"""
AMICABLE NUMBERS
"""
import math
import unittest


def divisors_sum(number):
    """
    Get the sum of proper divisors of number.
    """
    result = [1, ]
    d = 2
    while d <= math.sqrt(number):
        if number % d == 0:
            result.append(d)
            result.append(number // d)
        d += 1
    return sum(set(result))


class Problem21Test(unittest.TestCase):
    def test_divisors_sum(self):
        self.assertEquals(divisors_sum(220), 284)
        self.assertEquals(divisors_sum(284), 220)


# unittest.main()


if __name__ == "__main__":
    """
    Let d(n) be defined as the sum of proper divisors of n
    (numbers less than n which divide evenly into n).

    If d(a) = b and d(b) = a, where a ≠ b,
    then a and b are an amicable pair
    and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are
    1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
    The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    """
    # for x in range(6, 300):
    amicable_pairs = []
    # we can start with 220 as it is the minimum amicable number
    for a in range(220, 10000):
        d_a = divisors_sum(a)
        if d_a > a:
            d_b = divisors_sum(d_a)
            if d_b == a and a != d_a:
                amicable_pairs.append((a, d_a))
    print("Problem 21: amicable numbers")
    print(amicable_pairs)
    print(sum([i[0] + i[1] for i in amicable_pairs]))
