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
    numbers = list(range(2, limit + 1))
    while numbers:
        x = numbers.pop(0)
        yield x
        sieved = set(range(x * x, limit + 1, x))
        numbers = list(set(numbers) - sieved)
        numbers.sort()


class PrimeTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(19))

    def test_primes(self):
        self.assertEqual(list(primes(25)), [2, 3, 5, 7, 11, 13, 17, 19, 23])


# unittest.main()
