# PRIME PERMUTATIONS

"""
The arithmetic sequence, 1487, 4817, 8147,
in which each of the terms increases by 3330,
is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three
1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating
the three terms in this sequence?
"""

import sys
from itertools import permutations as iter_permutations
from utils.prime_numbers import primes


if __name__ == "__main__":
    print(__doc__)
    print("*" * 55)

    prime_numbers = list(primes(9999))

    for number in range(1009, 9999):
        if number in prime_numbers:
            string_permutations = set(iter_permutations([i for i in str(number)], 4))
            string_permutations = list(filter(lambda x: x[0] != "0", string_permutations))
            permutations = [int("".join(i)) for i in string_permutations]
            permutations = list(filter(lambda x: x in prime_numbers, permutations))
            if len(permutations) < 3:
                continue
            else:
                permutations.sort()
                for i in range(1, len(permutations)):
                    diff = permutations[i] - permutations[i - 1]
                    if permutations[i] + diff in permutations:
                        print(f"{permutations[i-1]}{permutations[i]}{permutations[i]+diff}")
                        sys.exit()
