# DIGIT FIFTH POWERS

"""
Surprisingly there are only three numbers that can be written
as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
    As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written
as the sum of fifth powers of their digits.
"""


def is_sum_of_nth_digit_powers(number, power):
    return sum([int(digit) ** power for digit in str(number)]) == number


if __name__ == "__main__":
    print(__doc__)
    print("*" * 50)
    answer = 0
    for n in range(101, 1000000):
        if is_sum_of_nth_digit_powers(n, 5):
            print(n)
            answer += n
    print(f"The answer is {answer}")
