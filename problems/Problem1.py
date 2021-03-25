"""
If we list all the natural numbers below 10
that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multipliers_sum(below):
    numbers = [x for x in range(1, below) if x % 3 == 0 or x % 5 == 0]
    return sum(numbers)


if __name__ == "__main__":
    print(multipliers_sum(1000))
