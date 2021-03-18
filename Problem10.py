"""
SUMMATION OF PRIMES
"""
import unittest

from utils.prime_numbers import primes


def prime_summation(limit):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """
    numbers = list(primes(limit))
    return sum(numbers)


class ProblemTenTest(unittest.TestCase):
    def test_prime_summation(self):
        self.assertEqual(prime_summation(limit=10), 17)


# unittest.main()


if __name__ == "__main__":
    print("Summation of primes below 2 million")
    print(prime_summation(2000000))
