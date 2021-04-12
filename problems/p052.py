# PERMUTED MULTIPLIERS

"""
It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
and 6x, contain the same digits.
"""


if __name__ == "__main__":
    print(__doc__)
    print("*" * 65)

    for n in range(100, 1000000):
        digits = [i for i in str(n)]
        digits.sort()
        found = True
        for multiplier in range(2, 7):
            multiple_digits = [i for i in str(n * multiplier)]
            multiple_digits.sort()
            if digits != multiple_digits:
                found = False
                break
        if found:
            print(n)
            break
