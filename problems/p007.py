# 10001ST PRIME

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from utils.prime_numbers import primes


def nth_prime(n):
    prime_numbers = []
    limit = 150000
    while len(prime_numbers) < n:
        prime_numbers = list(primes(limit))
        if len(prime_numbers) >= n:
            return prime_numbers[n - 1]
        limit += 1000
    return 2


if __name__ == "__main__":
    print(__doc__)
    print("*" * 50)
    print(nth_prime(10001))
