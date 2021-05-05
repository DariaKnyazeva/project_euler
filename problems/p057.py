# SQUARE ROOT CONVERGENTS
"""
It is possible to show that the square root of two
can be expressed as an infinite continued fraction.

                     1
           1 +  ______________  ...
sqrt(2) =        2   +    1
                       _______

By expanding this for the first four iterations, we get:

 1 + 1/2 = 1.5

 1 + 1/(2 + 1/2) = 7/5 = 1.4

 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...

 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379

The next three expansions are 99/70, 239/169. and 577/408,
but the eighth expansion, 1393/985, is the first example where
the number of digits in the numerator exceeds the number of digits
in the denominator.

In the first one-thousand expansions, how many fractions contain
a numerator with more digits than the denominator?
"""


def expansion(x):
    return 2 + 1 / 2


if __name__ == "__main__":
    print(__doc__)
    print("*" * 55)

    p_2, p_1 = 1, 3
    q_2, q_1 = 1, 2

    count = 0
    for i in range(1, 1000):
        p_next = 2 * p_1 + p_2
        p_2, p_1 = p_1, p_next
        q_next = 2 * q_1 + q_2
        q_2, q_1 = q_1, q_next
        if len(str(p_next)) > len(str(q_next)):
            count += 1
    print(count)
