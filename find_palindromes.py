import unittest
import math
import re
"""
find the longest palindrome in a string. 
"""

tests = [
	("madam I'm Adam", 										["madam"]), 				# one palindrome
	("I ama containing two three letter palindromes: dud", 	["ama", 'dud']),			# two
	("palindromeemordnilap", 								["palindromeemordnilap"]), 	# whole string
	("A longnol palindrom and a short oneno", 				["longnol"]),				# two palindroms, one longer
	("pop dood mum, eve",									['dood']),								
]


class PalindromeFinder:

	def find_in(self, string):
		# loop through strings from pos 1 to len -2
		# look back, look fwd, store palindromic patterns in an list
		# return list
		palindromes = []
		words = string.split(' ')
		for word in words:
			word = self._clean_word(word)
			if self._is_palindrome(word):
				palindromes.append(word)
		return palindromes

	@staticmethod
	def _clean_word(word):
		"""
		lowercase, remove punctuation
		"""
		word = word.lower()
		# ah, this is a case for a regex
		word = re.sub(r'^[^0-9a-z]*', "", word)
		word = re.sub(r'[^0-9a-z]*$', "", word)
		return word

	@staticmethod
	def _is_palindrome(str):
		strlen = len(str)
		midpoint_lft = midpoint_rght = int(math.ceil(strlen/2))
		even = strlen % 2
		if not even:
			midpoint_lft -= 1
		for x in range(0, midpoint_lft+1):
			back  = str[midpoint_lft-x]
			forwd = str[midpoint_rght+x]
			if back != forwd:
				return False
		return True



class TestPDfinder(unittest.TestCase):

	def test_is_palindrome_method(self):
		pdf = PalindromeFinder()
		self.assertTrue(pdf._is_palindrome('madam'))
		self.assertTrue(pdf._is_palindrome('madadam'))
		self.assertTrue(pdf._is_palindrome('maam'))
		self.assertFalse(pdf._is_palindrome('madame'))
		self.assertFalse(pdf._is_palindrome('madamel'))
		self.assertFalse(pdf._is_palindrome('adam'))

	def test_is_palindrom_only_1st_andl_last_differnce(self):
		pdf = PalindromeFinder()
		self.assertFalse(pdf._is_palindrome('letter'))


	def test_is_palindrom_short_words(self):
		pdf = PalindromeFinder()
		self.assertFalse(pdf._is_palindrome('two'))
		self.assertTrue(pdf._is_palindrome('i'))

	def test_clean_word_method(self):
		pdf = PalindromeFinder()
		self.assertEquals(pdf._clean_word("!madam"), "madam")
		self.assertEquals(pdf._clean_word("madam,"), "madam")
		self.assertEquals(pdf._clean_word("'madam',"), "madam")
		self.assertEquals(pdf._clean_word("Groovy!"), "groovy")
		self.assertEquals(pdf._clean_word("I'm"), "i'm")

	def test_finding_one_simple_palindrome(self):
		pdf = PalindromeFinder()
		self.assertEquals(pdf.find_in("madam I'm Adam"), ["madam"])

	def test_finding_two_palindromes(self):
		pdf = PalindromeFinder()
		self.assertEquals(pdf.find_in("I ama containing two three letter palindromes: dud"), ["i", "ama", "dud"])

	def test_whole_string_is_palindromes(self):
		pdf = PalindromeFinder()
		self.assertEquals(pdf.find_in("palindromeemordnilap"), ["palindromeemordnilap"])



if __name__ == '__main__':
	unittest.main()

