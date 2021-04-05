# SUMMATION OF PRIMES

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from utils.prime_numbers import primes


def prime_summation(limit):
    numbers = list(primes(limit))
    return sum(numbers)


if __name__ == "__main__":
    print(__doc__)
    print("*" * 50)
    print(prime_summation(2000000))
