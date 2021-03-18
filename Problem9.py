"""
SPECIAL PYTHAGOREAN TRIPLET
"""
import math
import unittest


def is_pythagorian(a, b, c):
    return a * a + b * b == c * c


def get_pythagorian_triplet(a, b):
    return math.sqrt(a * a + b * b)


def pythagorean_triplet(triplet_sum=36):
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    # In a Pythagorean triplet one side is divisible by 3, one by 4 and one by 5
    for a in range(3, 1000, 3):
        for b in range(4, 2000, 4):
            c = math.sqrt(a * a + b * b)
            if float(c) == int(c):
                if a + b + c == triplet_sum:
                    return a * b * c
            else:
                continue


class ProblemNineTest(unittest.TestCase):
    def test_pythagorean_triplet(self):
        self.assertEqual(pythagorean_triplet(triplet_sum=36), 1620)


# unittest.main()


if __name__ == "__main__":
    print("Problem 9: Special Pythagorean triplet")
    print(pythagorean_triplet(triplet_sum=1000))
