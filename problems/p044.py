# PENTAGONAL NUMBERS

"""
Pentagonal numbers are generated by the formula, Pn=n(3nā1)/2.
The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
However, their difference, 70 ā 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which
their sum and difference are pentagonal and
D = |Pk ā Pj| is minimised; what is the value of D?
"""

import math
import sys


def pentagonals(size):
    for n in range(1, size + 1):
        yield get_pentagonal(n)


def get_pentagonal(n):
    return int(0.5 * n * (3 * n - 1))


def is_pentagonal(n):
    # the inverse function
    pentagonal = (math.sqrt(1 + 24 * n) + 1.0) / 6.0
    return int(pentagonal) == pentagonal


if __name__ == "__main__":
    print(__doc__)
    print("*" * 55)

    i = 1
    while True:
        i += 1
        n = get_pentagonal(i)
        for j in range(i - 1, 0, -1):
            m = get_pentagonal(j)
            if is_pentagonal(n - m) and is_pentagonal(n + m):
                result = n - m
                print(result)
                sys.exit(0)
