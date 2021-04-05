# QUADRATIC PRIMES

"""
Euler discovered the remarkable quadratic formula:

n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer values
0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40 * (40 + 1) is divisible by 41,
and certainly when n=41, 41^2 + 41 + 41  is clearly divisible by 41.

The incredible formula n^2 - 79n +1601 was discovered, which produces 80 primes
for the consecutive values 0 <= n <= 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
    n^2 + an + b, where |a| < 1000 and |b| <= 1000

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

from utils.prime_numbers import primes


def euler(n, a, b):
    return n * n + a * n + b


if __name__ == "__main__":
    prime_numbers = list(primes(1000))
    print(__doc__)
    print("*" * 90)
    max_consecutive = 0
    max_a = 0
    max_b = 0
    for a in range(-999, 0):  # a is rather negative
        # b has to be positive and it has to be prime itself,
        # the max prime below 1000 is 997
        for b in range(998):
            n = 0
            while euler(n, a, b) in prime_numbers:
                n += 1
            if n > max_consecutive:
                max_consecutive = n
                max_a = a
                max_b = b
    print(f"Max consecutive primes {max_consecutive}")
    print(f"a = {max_a}")
    print(f"b = {max_b}")
    print(f"a * b = {max_a * max_b}")
