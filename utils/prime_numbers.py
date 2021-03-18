import math
import unittest


def is_prime(number):
    """
    Returns True if the number is prime, False otherwise.
    """
    if number % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False

    return True


def primes(limit):
    """
    Returns generator of prime numbers below specified limit
    using Eratosthenes Sieve algorithm

    @param limit: int
    """
    multiples = set()
    for i in range(2, limit + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, limit + 1, i))


class PrimeTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(19))

    def test_primes(self):
        self.assertEqual(list(primes(25)), [2, 3, 5, 7, 11, 13, 17, 19, 23])


# unittest.main()
