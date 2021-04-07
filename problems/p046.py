# GOLDBACK'S OTHER CONJECTURE

"""
It was proposed by Christian Goldbach that every odd
composite number can be written as the sum of a prime
and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written
as the sum of a prime and twice a square?
"""

from utils.prime_numbers import primes


if __name__ == "__main__":
    print(__doc__)
    print("*" * 60)

    prime_numbers = list(primes(1000000))
    squares = [i * i for i in range(1, 1001)]

    for number in range(35, 1000000, 2):
        # print(number)
        if number in prime_numbers:
            continue
        found = False
        for prime in prime_numbers:
            if prime > number:
                break
            square = (number - prime) / 2
            if square in squares:
                found = True
                break
        if not found:
            print(number)
            break
