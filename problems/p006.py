# SUM SQUARE DIFFRENCE

"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2  = 55^2 = 3025

Hence the difference between the sum of the squares
of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640.

Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.
"""


def arithmetic_progression(a1, an, n):
    return (a1 + an) * n / 2


def sum_square_difference(limit=10):
    ap = arithmetic_progression(1, limit, limit)
    return ap * ap - sum([i * i for i in range(1, limit + 1)])


if __name__ == "__main__":
    print(__doc__)
    print("*" * 65)
    print(sum_square_difference(limit=100))
