import math
import unittest


def c_n_k(n, k):
    """
    Returns number of combinations of n by k
    """
    assert k <= n
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))


class CombinatoricsTest(unittest.TestCase):
    def test_c_n_k(self):
        self.assertEqual(c_n_k(7, 4), 35)
        self.assertEqual(c_n_k(10, 3), 120)
        self.assertEqual(c_n_k(10, 10), 1)
        self.assertEqual(c_n_k(10, 9), 10)


# unittest.main()
