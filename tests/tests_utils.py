import unittest

from utils.combinatorics import c_n_k
from utils.prime_numbers import is_prime, primes
from utils.triangular_numbers import triangulars


class CombinatoricsTest(unittest.TestCase):
    def test_c_n_k(self):
        self.assertEqual(c_n_k(7, 4), 35)
        self.assertEqual(c_n_k(10, 3), 120)
        self.assertEqual(c_n_k(10, 10), 1)
        self.assertEqual(c_n_k(10, 9), 10)


class PrimeTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(19))

    def test_primes(self):
        self.assertEqual(list(primes(25)), [2, 3, 5, 7, 11, 13, 17, 19, 23])


class TriangularTest(unittest.TestCase):
    def test_triangulars(self):
        self.assertEqual(list(triangulars(7)), [1, 3, 6, 10, 15, 21, 28])


unittest.main()
