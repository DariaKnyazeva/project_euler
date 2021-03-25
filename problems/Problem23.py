"""
NON-ABUDANT SUMS
"""
import itertools
import math
import datetime


def is_abudant(number):
    """
    Returns True if the number n is abudant.
    A number n is called abundant if the sum
    of its proper divisors exceeds n.
    """
    result = [1, ]
    d = 2
    while d <= math.sqrt(number):
        if number % d == 0:
            result.append(d)
            result.append(number // d)
        d += 1
    return sum(set(result)) > number


def abundants(n):
    """
    Return abundant numbers generator
    """
    for i in range(12, n):
        if is_abudant(i):
            yield i


def is_abundant_sum(n, abundant_numbers):
    for idx, a in enumerate(abundant_numbers):
        if a > n:
            return False
        if n - a in abundant_numbers:
            return True
    return False


if __name__ == "__main__":
    """
    A perfect number is a number for which the sum of its proper divisors
    is exactly equal to the number.
    For example, the sum of the proper divisors of 28
    would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors
    is less than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
    the smallest number that can be written as the sum of two abundant numbers is 24.
    By mathematical analysis, it can be shown that all integers greater than 28123
    can be written as the sum of two abundant numbers.
    However, this upper limit cannot be reduced any further by analysis even though
    it is known that the greatest number that cannot be expressed as the sum of
    two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum
    of two abundant numbers.
    """
    print("Problem 24: Non-abundant sums")
    limit = 28124
    abundant_nums = list(abundants(limit))
    print(datetime.datetime.now())
    ab_sums = ([i[0] + i[1] for i in itertools.combinations(abundant_nums, 2)])
    ab_doubles = [i * 2 for i in abundant_nums if i < limit / 2]
    ab_sums.extend(ab_doubles)
    non_ab_sums = set(range(1, limit)).difference(set(ab_sums))
    print(sum(non_ab_sums))
    print(datetime.datetime.now())
