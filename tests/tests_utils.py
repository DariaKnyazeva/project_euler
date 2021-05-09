import unittest

from utils.combinatorics import c_n_k
from utils.pandigital import is_pandigital
from utils.prime_numbers import is_prime, primes, rotation, circular_primes
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

    def test_primes_include_limit(self):
        self.assertEqual(list(primes(11)), [2, 3, 5, 7, 11])


class TriangularTest(unittest.TestCase):
    def test_triangulars(self):
        self.assertEqual(list(triangulars(7)), [1, 3, 6, 10, 15, 21, 28])


class CircularPrimesTest(unittest.TestCase):
    def test_rotation(self):
        rotations = rotation(197)
        self.assertEqual(3, len(rotations))
        self.assertTrue(197 in rotations)
        self.assertTrue(971 in rotations)
        self.assertTrue(719 in rotations)

        rotations = rotation(1234)
        self.assertEqual(4, len(rotations))
        self.assertTrue(1234 in rotations)
        self.assertTrue(2341 in rotations)
        self.assertTrue(3412 in rotations)
        self.assertTrue(4123 in rotations)

    def test_circular_primes(self):
        self.assertEqual(list(circular_primes(100)),
                         [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, ])


class PandigitalTest(unittest.TestCase):
    def test_is_pandigital(self):
        self.assertFalse(is_pandigital(234))
        self.assertTrue(is_pandigital(24315, limit=5))


unittest.main()
