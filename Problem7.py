"""
10001st PRIME
"""
import unittest
from utils.prime_numbers import primes


def nth_prime(n):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    """
    prime_numbers = []
    limit = 150000
    while len(prime_numbers) < n:
        prime_numbers = list(primes(limit))
        if len(prime_numbers) >= n:
            return prime_numbers[n - 1]
        limit += 1000
    return 2


class ProblemSevenTest(unittest.TestCase):
    def test_nth_prime(self):
        self.assertEqual(nth_prime(6), 13)


# unittest.main()


if __name__ == "__main__":
    print(nth_prime(10001))
