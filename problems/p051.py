# PRIME DIGIT REPLACEMENTS

"""
By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes
among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""

import sys
from utils.prime_numbers import primes


if __name__ == "__main__":
    print(__doc__)
    print("*" * 60)

    prs = primes(1000000)
    prs = list(filter(lambda x: x > 100000, prs))

    for n in prs:
        number = str(n)
        for i in range(10):
            count = 1
            if str(i) in number and number.index(str(i)) != number.rindex(str(i)):
                for j in range(i + 1, 10):
                    new_number = int(number.replace(str(i), str(j)))
                    if new_number != n and new_number in prs:
                        count += 1
                    if count > 7:
                        print(n)
                        sys.exit()
