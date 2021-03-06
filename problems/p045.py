# TRIANGULAR, PENTAGONAL AND HEXAGONAL

"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle        Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
Pentagonal      Pn=n(3n−1)/2        1, 5, 12, 22, 35, ...
Hexagonal       Hn=n(2n−1)      1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

import math


def is_pentagonal(n):
    # the inverse function
    pentagonal = (math.sqrt(1 + 24 * n) + 1.0) / 6.0
    return int(pentagonal) == pentagonal


def is_hexagonal(n):
    hexagonal = (math.sqrt(1 + 8 * n) + 1.0) / 4.0
    return int(hexagonal) == hexagonal


def triangulars(start, end):
    for n in range(start, end + 1):
        yield 0.5 * n * (n + 1)


if __name__ == "__main__":
    print(__doc__)
    print("*" * 70)
    # start from T286 as we need to find the suitable number after T285
    numbers = triangulars(286, 100000)
    for n in numbers:
        if is_hexagonal(n) and is_pentagonal(n):
            print(n)
            break
