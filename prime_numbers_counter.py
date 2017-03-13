"""
This code written in response to a Codility test.

The Problem:
write a function that returns the number of prime numbers between a given range
so, for example....

func(1, 10)
returns 4 because 3, 5, 7, 9 are prime numbers in that range

func(9, 21)
returns 5
because 9, 11, 13, 17, 19 are prime numbers

"""
import unittest
import math


KNOWN_PRIMES = [
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 
83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 
179, 181, 191, 193, 197, 199
]

# thus list precalculated by precalculate_pseudo_primes()
CALCULATED_PSEUDOPRIMES = [
341, 561, 645, 1105, 1387, 1729, 1905, 2047, 2465, 2701, 2821, 3277, 4033, 4369, 4371, 4681, 5461, 6601, 7957, 8321, 8481, 8911,
10261,10585,
11305,
12801,
13741,13747,13981,
14491,
15709,15841,
16705,
18705,18721,
19951,
23001,23377,25761,29341,
30121,30889,31417,31609,31621,33153,34945,35333,39865,
41041,41665,42799,46657,49141,49981,
52633,55245,57421,
60701,60787,62745,63973,65077,65281,68101,
72885,74665,75361,
80581,83333,83665,85489,87249,88357,88561,
90751,91001,93961,
101101,104653,107185,
113201,115921,
121465,123251,126217,129889,129921,
130561,137149,
149281,
150851,154101,157641,158369,
162193,162401,164737,
172081,176149,
181901,188057,188461,
194221,196021,196093,
204001,206601,208465,
212421,215265,215749,219781,
220729,223345,226801,228241,
233017,
241001,249841,
252601,253241,256999,258511,
264773,266305,
271951,272251,275887,276013,278545,
280601,282133,284581,285541,289941,
294271,294409,
314821,318361,
323713,
332949,334153,
340561,341497,348161,
357761,
367081,387731,
390937,396271,399001,
401401,
410041,
422659,423793,427233,
435671,
443719,448921,449065,
451905,452051,458989,
464185,
476971,
481573,486737,488881,489997,
493697,493885]


TEST_PSEUDOPRIMES = [
341, 561, 645, 1105,
1387, 1729,
1905, 2047,
2465, 2701,
2821, 3277,
4033, 4369,
4371, 4681,
5461, 6601,
7957, 8321,
8481, 8911,
10261, 10585,
11305, 12801,
13741, 13747,
13981, 14491,
15709, 15841,
16705, 18705,
18721, 19951,
23001, 23377,
25761, 29341]


def primecount(a, b):
	count = 0
	for x in range(a, b+1):
		count += _is_prime(x)
	return count

def _is_prime(x):
	"""
	return 1 if number is prime
	return 0 if number not prime
	"""
	prime = _is_prime_simple(x)
	if prime:
#		prime = _is_prime_full(x)
		prime = x not in CALCULATED_PSEUDOPRIMES
	return 1 if prime else 0 

def _is_prime_simple(x):
	"""
	we do the 'cheap' calculations here
	special casea for 1 & 2, 
	returning even numbers as False
	and then using fermat's little theorem
	"""
	if x == 1:
		return False
	if x == 2:
		return True
	if x != 2 and x % 2 == 0:
		return False
	"""
	Fermat's little theorem states that...
	if p is a prime number, then for any integer a, the number a^p − a is an integer multiple of p
	For example, if a = 2 and p = 7, 27 = 128, and 128 − 2 = 7 × 18 is an integer multiple of 7.
	"""
	a = 2
	return ((a**x) - a) % x == 0

def _is_prime_full(x):
	"""
	fermat's little theorem returns some pseudoprimes that we must filter out
	this is a more rigorous (but more expensive) check
	"""
	for y in range(3, math.floor(x/2), 2):
		# loop through odd numbers, upto half-way to the target
		# checking for a valid divisor
		if x % y == 0:
			return False
	return True

def find_pseudoprimes(a, b):
	"""
	we can use this to precalculate pseudoprimes if we know the 
	range we need to cover
	"""
	for x in range(a, b+1):
		simple = _is_prime_simple(x)
		if simple and not _is_prime_full(x):
			yield x



class TestPrimeSimple(unittest.TestCase):

	def test_is_prime_simple_on_even_numbers(self):
		for x in range(4, 200, 2):
			res = _is_prime_simple(x)
			self.assertFalse(res)

	def test_is_prime_simple_on_known_primes(self):
		for x in KNOWN_PRIMES:
			res = _is_prime_simple(x)
			self.assertTrue(res)

	def test_is_prime_simple_on_known_pseudoprimes(self):
		"""
		these are NOT prime numbers, but our simple function thinks they are...
		this test proves the need for our fuller test
		"""
		for x in TEST_PSEUDOPRIMES:
			res = _is_prime_simple(x)
			self.assertTrue(res)


class TestPrimeFull(unittest.TestCase):

	def test_is_prime_full_on_known_primes(self):
		for x in KNOWN_PRIMES:
			res = _is_prime_full(x)
			self.assertTrue(res)

	def test_is_prime_full_on_known_pseudoprimes(self):
		for x in TEST_PSEUDOPRIMES:
			res = _is_prime_full(x)
			self.assertFalse(res)


class TestPrimeCount(unittest.TestCase):

	def test_simple(self):
		self.assertEqual(primecount(1, 10), 4)

	def test_left_number_included(self):
		self.assertEqual(primecount(3, 10), 3)

	def test_right_number_included(self):
		self.assertEqual(primecount(3, 11), 4)

	def test_using_known_primes_list(self):
		self.assertEqual(primecount(KNOWN_PRIMES[0], KNOWN_PRIMES[-1]), len(KNOWN_PRIMES))

	def test_no_primes_found(self):
		self.assertEqual(primecount(20, 22), 0)

	def test_primes_count_on_large_range(self):
		assert primecount(0 , 50000) > 0


def precalculate_pseudo_primes(a, b):
	for x in find_pseudoprimes(a, b):
		print(x)


if __name__ == "__main__":
	unittest.main() 
#	precalculate_pseudo_primes(0, 500000)
