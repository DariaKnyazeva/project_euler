import unittest

from problems.Problem1 import multipliers_sum
from problems.Problem3 import largest_prime_factor
from problems.Problem4 import is_palindrom, largest_palindrome
from problems.Problem5 import smallest_multiply
from problems.Problem6 import sum_square_difference
from problems.Problem7 import nth_prime
from problems.Problem8 import largest_product_in_series
from problems.Problem9 import pythagorean_triplet
from problems.Problem10 import prime_summation
from problems.Problem12 import divisors, highly_divisible_triangular
from problems.Problem14 import collatz_sequence
from problems.Problem18 import Tree
from problems.Problem21 import divisors_sum
from problems.Problem26 import decimal_repr


class ProblemOneTest(unittest.TestCase):
    def test_below_ten(self):
        self.assertEqual(multipliers_sum(10), 23)


class ProblemThreeTest(unittest.TestCase):
    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)


class PalindromTest(unittest.TestCase):
    def test_is_palindrom(self):
        self.assertTrue(is_palindrom(9009))
        self.assertFalse(is_palindrom(9005))
        self.assertTrue(is_palindrom(90109))
        self.assertFalse(is_palindrom(90105))

    def test_largest_palindrom(self):
        self.assertEqual(largest_palindrome(n_digits=2), 9009)


class ProblemFiveTest(unittest.TestCase):
    def test_smallest_multiply(self):
        self.assertEqual(smallest_multiply(10), 2520)
        self.assertEqual(smallest_multiply(20), 232792560)


class ProbleSixTest(unittest.TestCase):
    def test_sum_square_difference(self):
        self.assertEqual(sum_square_difference(10), 2640)


class ProblemSevenTest(unittest.TestCase):
    def test_nth_prime(self):
        self.assertEqual(nth_prime(6), 13)


class ProblemEightTest(unittest.TestCase):
    def test_largest_product_in_series(self):
        self.assertEqual(largest_product_in_series(ajacent_digits_number=4), 5832)


class ProblemNineTest(unittest.TestCase):
    def test_pythagorean_triplet(self):
        self.assertEqual(pythagorean_triplet(triplet_sum=36), 1620)


class ProblemTenTest(unittest.TestCase):
    def test_prime_summation(self):
        self.assertEqual(prime_summation(limit=10), 17)


class ProblemTwelveTest(unittest.TestCase):

    def test_get_divisors(self):
        self.assertEqual(divisors(15), {1, 3, 5, 15})

    def test_highly_divisible_triangular(self):
        self.assertEqual(highly_divisible_triangular(5), 28)


class Problem14Test(unittest.TestCase):
    def test_collatz_sequence(self):
        self.assertEqual(list(collatz_sequence(13)),
                         [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])


class Problem18Test(unittest.TestCase):
    def test_triangle_path(self):
        triangle = [
            [3, ],
            [7, 4, ],
            [2, 4, 6, ],
            [8, 5, 9, 3, ],
        ]

        tree = Tree(triangle)
        self.assertEqual(tree.max_path_sum(tree.root), 23)


class Problem21Test(unittest.TestCase):
    def test_divisors_sum(self):
        self.assertEqual(divisors_sum(220), 284)
        self.assertEqual(divisors_sum(284), 220)


class Problem26Test(unittest.TestCase):
    def test_decimal_repr(self):
        self.assertEqual(decimal_repr(1, 2), "0.5")
        self.assertEqual(decimal_repr(1, 4), "0.25")
        self.assertEqual(decimal_repr(1, 8), "0.125")
        self.assertEqual(decimal_repr(1, 3), "0.(3)")
        self.assertEqual(decimal_repr(1, 6), "0.1(6)")
        self.assertEqual(decimal_repr(1, 7), "0.(142857)")
        self.assertEqual(decimal_repr(1, 64), "0.015625")
        self.assertEqual(decimal_repr(1, 999, min_cycle_len=2), "0.(001)")
        self.assertEqual(decimal_repr(1, 29, min_cycle_len=6), "0.(0344827586206896551724137931)")


unittest.main()
