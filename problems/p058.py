# SPIRAL PRIMES

"""
Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49 50

It is interesting to note that the odd squares lie along the bottom
right diagonal, but what is more interesting is that 8 out of the 13
numbers lying along both diagonals are prime; that is,
a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above,
a square spiral with side length 9 will be formed. If this process
is continued, what is the side length of the square spiral for which
the ratio of primes along both diagonals first falls below 10%?
"""
from utils.prime_numbers import is_prime


def _additional(diagonal: int, square_side: int):
    result = []
    for add in range(square_side - 1, square_side, 2):
        for i in range(4):
            diagonal += add
            result.append(diagonal)
    return result


if __name__ == "__main__":
    print(__doc__)
    print('*' * 65)

    diagonal = 49
    square_side = 9
    total_count = 13
    prime_count = 8
    while True:
        result = _additional(diagonal, square_side)
        diagonal = result[-1]
        total_count += 4
        prime_count += len([x for x in result if is_prime(x)])
        percentage = prime_count / total_count
        print(f"{square_side}: {percentage}")
        square_side += 2
        if percentage < 0.1:
            break
