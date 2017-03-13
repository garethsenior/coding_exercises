"""

given an array
and a 'sub' array

can you find the sub-sequnce in the larger array?

"""

import unittest
import string

def array_find(array, subarray):
	"""
	returns -1 ir sub-array is not found
	otherwise return starting index of sub array
	find ALL or find first?
	"""
	stringed_arr = [str(a) for a in array]
	punc = string.punctuation
	for i in range(0, len(punc)-1):
		# check this sequence is not in any of the list entries
		sep = punc[i:i+2]
		try:
			next(x for x in stringed_arr if x.find(sep) != -1)
		except StopIteration:
			break

	array_str = sep.join(stringed_arr)
	subarray_str = sep.join([str(s) for s in subarray])
	index = array_str.find(subarray_str)
	if index == -1:
		return -1
	index = int(index / 3)
	return index



class TestFindSubArray(unittest.TestCase):

	def test_array_not_found(self):
		arr = [0, 1, 2, 3, 4, 5, 6]
		sub = [10]
		self.assertEqual(array_find(arr, sub), -1)

	def test_array_found_at_0(self):
		arr = [0, 1, 2, 3, 4, 5, 6]
		sub = [0, 1, 2, 3, 4]
		self.assertEqual(array_find(arr, sub), 0)


	def test_array_found_at_2(self):
		arr = [0, 1, 2, 3, 4, 5, 6]
		sub = [2, 3, 4]
		self.assertEqual(array_find(arr, sub), 2)

	def test_array_found_at_6(self):
		arr = [0, 1, 2, 3, 4, 5, 6]
		sub = [6]
		self.assertEqual(array_find(arr, sub), 6)

	def test_pipes_in_patterns(self):
		arr = ["|", "#$", "%", "|", "||"]
		sub = ["|", "||"]
		self.assertEqual(array_find(arr, sub), 3)



if __name__ == "__main__":
	unittest.main()