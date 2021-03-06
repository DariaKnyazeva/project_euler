# CHAMPERNOWNE's CONSTANT

"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""


if __name__ == "__main__":
    print(__doc__)
    print("*" * 60)

    champernowne = "".join([str(i) for i in range(1, 1000000)])
    indexes = [99, 999, 9999, 99999, 999999]
    answer = 1
    for idx in indexes:
        answer *= int(champernowne[idx])
    print(answer)
