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


def rotation(n):
    """
    Return rotations of digits for the number n.

    For any positive integer, we define a digit rotation
    as moving the first digit to the end of the number
    until we get the initial number
    For example, the rotations of number 1234 are 2341, 3412, 4123, 1234
    """
    rotations = set()
    for i in range(len(str(n))):
        m = int(str(n)[i:] + str(n)[:i])
        rotations.add(m)
    return rotations


def circular_primes(limit):
    """
    Returns generator of circular primes below limit.

    The number, 197, is called a circular prime because
    all rotations of the digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100:
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
    """
    prime_nums = list(primes(limit))
    for n in prime_nums:
        rotations = rotation(n)
        if len([i for i in rotations if i in prime_nums]) == len(rotations):
            yield n
