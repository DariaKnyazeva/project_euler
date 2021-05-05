import math
from typing import Generator, List, Set


def is_prime(number: int) -> bool:
    """
    Returns True if the number is prime, False otherwise.
    """
    if number % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False

    return True


def primes(limit: int) -> Generator[int, None, None]:
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


def write_to_file_primes_below(limit: int) -> None:
    numbers = primes(limit)
    filepath = f"data/primes_{limit}.txt"
    with open(filepath, "w") as f:
        for n in numbers:
            f.write(f"{str(n)}\n")


def read_primes_from_file(limit: int) -> List[int]:
    filepath = f"data/primes_{limit}.txt"
    with open(filepath, "r") as f:
        return [int(n) for n in f.readlines()]


def rotation(n: int) -> Set[int]:
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


def circular_primes(limit: int) -> Generator[int, None, None]:
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
