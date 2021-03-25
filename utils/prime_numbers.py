import math


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
