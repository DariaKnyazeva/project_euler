"""
HIGHLY DIVISIBLE TRIANGULAR NUMBER
"""
import math
import unittest

from utils.triangular_numbers import triangulars


def divisors(number):
    """
    Get all divisors of the number.
    """
    result = [1, number]
    d = 2
    while d <= math.sqrt(number):
        if number % d == 0:
            result.append(d)
            result.append(number // d)
        d += 1
    return set(result)


def highly_divisible_triangular(divisors_count=5):
    """
    The sequence of triangle numbers is generated by adding the natural numbers.
    So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

    The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?
    """
    sequence = triangulars(100000)
    for i in sequence:
        if len(divisors(i)) > divisors_count:
            return i
    return None


class ProblemTwelveTest(unittest.TestCase):

    def test_get_divisors(self):
        self.assertEqual(divisors(15), {1, 3, 5, 15})

    def test_highly_divisible_triangular(self):
        self.assertEqual(highly_divisible_triangular(5), 28)


unittest.main()


if __name__ == "__main__":
    print("Problem 12: Highly divisible triangular number.")
    print(highly_divisible_triangular(500))