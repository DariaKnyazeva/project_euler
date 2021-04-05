# DOUBLE-BASE PALINDROMES

"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
"""


def is_palindrom(number):
    """
    Returns True if the number is palindrom, i. e. reads the same both ways
    but it should not have leading zeros
    """
    number = str(number)
    if number[-1] == '0':
        return False
    middle_index = int(len(number) / 2)
    if len(number) % 2 == 0:
        second_half = number[middle_index:]
    else:
        second_half = number[middle_index + 1:]
    return number[:middle_index] == second_half[::-1]


def to_binary(number):
    """
    Represents 10-base number in 2-base form.
    Returns string representation.
    """
    # import ipdb; ipdb.set_trace()
    result = []
    while number > 0:
        if number % 2 == 0:
            result.insert(0, '0')
            # number = number // 2
        else:
            result.insert(0, '1')
        number = number // 2
    return ''.join(result)


if __name__ == "__main__":
    print(__doc__)
    print("*" * 55)
    answer = 0
    for n in range(1, 1000000):
        if is_palindrom(n) and is_palindrom(to_binary(n)):
            print(n)
            answer += n
    print(answer)
