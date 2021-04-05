# PANDIGITAL PRODUCTS

"""
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity,
39 × 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure
to only include it once in your sum.
"""


def is_pandigital(n, limit=9):
    """
    Returns if the number n is Pandigital, i. e.
    if it makes use of all the digits 1 to limit exactly once;
    for example, the 5-digit number, 15234, is 1 through 5-limit pandigital.
    """
    digits = list(set(digit for digit in str(n)))
    if len(str(n)) > limit:
        return False
    digits.sort()
    return [int(d) for d in digits] == list(range(1, limit + 1))


if __name__ == "__main__":
    print(__doc__)
    print("*" * 55)
    answer = []
    for a in range(1, 100):
        for b in range(1, 2000):
            product = a * b
            number = f"{a}{b}{product}"
            if is_pandigital(number) and product not in answer:
                answer.append(product)
                print(f"{a}*{b}={product}")
    print(sum(answer))
