# PANDIGITAL PRIME

"""
We shall say that an n-digit number is pandigital if it
makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import itertools
from utils.prime_numbers import is_prime


if __name__ == "__main__":
    print(__doc__)
    print("*" * 55)

    for n in range(10, 1, -1):
        print(f"Checking {n - 1}-digit pandigitals")
        pandigitals = itertools.permutations(range(1, n))
        # order pandigitals lexicographically from largest to smallest
        pandigitals = ["".join([str(i) for i in sub]) for sub in pandigitals][::-1]
        for pandigital in pandigitals:
            # print(n)
            if is_prime(int(pandigital)):
                print(pandigital)
                break
