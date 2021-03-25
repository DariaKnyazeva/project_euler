"""
LARGEST PRIME FACTOR
"""
from utils.prime_numbers import primes


def largest_prime_factor(x):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

    @param x: int - the number to find the largest prome factor of.
    """
    prime_numbers = reversed(list(primes(10000)))
    for prime in prime_numbers:
        if x % prime == 0:
            return prime
    return x


if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
