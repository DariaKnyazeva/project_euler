# LARGEST PALINDROME PRODUCT

"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrom(number):
    """
    Returns True if the number is palindrom,
    i. e. reads the same both ways
    """
    number = str(number)
    middle_index = int(len(number) / 2)
    if len(number) % 2 == 0:
        second_half = number[middle_index:]
    else:
        second_half = number[middle_index + 1:]
    return number[:middle_index] == second_half[::-1]


def palindrome_products(n_digits=2):
    """
    Returns generator of the palindrome product of two n_digit numbers.
    """
    upper = int('9' * n_digits)
    lower = int('9' * (n_digits - 1))
    for a in range(upper, lower, -1):
        for b in range(upper, lower, -1):
            product = a * b
            if is_palindrom(product):
                # print("{} x {} = {}".format(a, b, product))
                yield product


def largest_palindrome(n_digits=2):
    return max(list(palindrome_products(n_digits=n_digits)))


if __name__ == "__main__":
    print(__doc__)
    print("*" * 70)
    print(largest_palindrome(n_digits=3))
