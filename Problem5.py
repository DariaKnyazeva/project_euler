"""
SMALLEST MULTIPLE
"""
from functools import reduce
import unittest

from utils.prime_numbers import primes


def smallest_multiply(limit=10):
    """
    2520 is the smallest number that can be divided by each
    of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible
    by all of the numbers from 1 to 20?
    """
    all_numbers = [i for i in range(2, limit + 1)]
    max_number = reduce((lambda x, y: x * y), all_numbers)
    # get all prime numbers below limit
    prime_numbers = list(primes(limit))
    # find the product of the above numbers
    prime_product = reduce((lambda x, y: x * y), prime_numbers)
    for num in range(prime_product, max_number, prime_product):
        divisions = [i for i in range(2, limit + 1) if num % i == 0]
        if len(divisions) == limit - 1:
            return num


class ProblemFiveTest(unittest.TestCase):
    def test_smallest_multiply(self):
        self.assertEqual(smallest_multiply(10), 2520)
        self.assertEqual(smallest_multiply(20), 232792560)


# unittest.main()

if __name__ == '__main__':
    print(smallest_multiply(limit=20))
