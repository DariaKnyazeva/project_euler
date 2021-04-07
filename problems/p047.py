# DISTINCT PRIME FACTORS

"""
The first two consecutive numbers to have
two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have
three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have
four distinct prime factors each.
What is the first of these numbers?
"""

from itertools import groupby
from operator import itemgetter
from utils.prime_numbers import primes

if __name__ == "__main__":
    print(__doc__)
    print("*" * 55)

    prime_nums = list(primes(200000))
    suit = []

    for i in range(14, 200000):
        if i not in prime_nums:
            consequetive_primes = []
            number = i
            while number != 1:
                for prime in prime_nums:
                    if number % prime == 0:
                        if prime not in consequetive_primes:
                            consequetive_primes.append(prime)
                        number = number // prime
                        break

            if len(consequetive_primes) > 3:
                suit.append(i)

    # Find consequetive elements in the list
    for k, g in groupby(enumerate(suit), key=lambda x: x[0] - x[1]):
        sequence = (list(map(itemgetter(1), g)))
        if len(sequence) == 4:
            print(sequence)
