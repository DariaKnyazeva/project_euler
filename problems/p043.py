# SUB-STRING DIVISIBILITY

"""
The number, 1406357289, is a 0 to 9 pandigital number
because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from utils.pandigital import pandigitats

if __name__ == "__main__":
    print(__doc__)
    print("*" * 65)

    divisors = {
        1: 2,
        2: 3,
        3: 5,
        4: 7,
        5: 11,
        6: 13,
        7: 17,
    }
    answer = 0
    numbers = pandigitats(10, zero_included=True, convert_to_int=False)

    for n in numbers:
        if n[0] == '0':
            # ignore leading zeros
            continue
        ok = True
        for idx in range(1, 8):
            if int(n[idx:idx + 3]) % divisors[idx] != 0:
                ok = False
                break
        if ok:
            print(n)
            answer += int(n)

    print(f"The sum is {answer}")
