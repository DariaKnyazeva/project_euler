"""
NUMBER SPIRAL DIAGONALS
"""


def spiral_diagonals(n):
    """
    Returns the sum of the diagonal elements of n x n matrix.

    The elements are filled in spiral starting 1 and moving to the right in a clockwise direction.

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    """
    start = 1
    result = start
    for i in range(2, n, 2):
        diag = range(start + i, n * n + 1, i)[:4]
        result += sum(diag)
        start = diag[-1]
    return result


if __name__ == "__main__":
    """
    Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.
    101 = 21 + 7 + 1 + 3 + 13 + 17 + 5 + 9 + 25

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
    """
    print("Problem 28: Number spiral diagonals")
    print(spiral_diagonals(1001))
