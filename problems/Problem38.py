"""
PANDIGITAL MULTIPLIERS
"""
# TODO: move to utils
from problems.Problem32 import is_pandigital


if __name__ == "__main__":
    """
    Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
    By concatenating each product we get the 1 to 9 pandigital, 192384576.
    We will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
    giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed
    as the concatenated product of an integer with (1,2, ... , n) where n > 1?
    """
    print("Problem 38: Pandigital multiples")
    # the possible largest pandigital number is 987654321.
    for n in range(9, 9786):  # iterate through numbers starting with "9"
        if str(n)[0] != '9':
            continue
        pandigital = ''
        for i in range(1, 3):
            pandigital += str(n * i)
        if is_pandigital(pandigital):
            print(pandigital)
