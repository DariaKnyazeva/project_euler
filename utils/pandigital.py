import itertools
from typing import List


def is_pandigital(n: int, limit: int = 9) -> bool:
    """
    Returns if the number n is Pandigital, i. e.
    if it makes use of all the digits 1 to limit exactly once;
    for example, the 5-digit number, 15234, is 1 through 5-limit pandigital.
    """
    digits = list(set(digit for digit in str(n)))
    if len(str(n)) > limit:
        return False
    digits.sort()
    return [int(d) for d in digits] == list(range(1, limit + 1))


def pandigitats(n_digits: int,
                zero_included: bool = False) -> List[int]:
    """
    Returns list of n-digit pandigital numbers ordered lexicographically
    """
    assert n_digits <= 10
    digits = range(n_digits) if zero_included else range(1, n_digits)
    pandigitals = itertools.permutations(digits)
    return [int("".join([str(i) for i in sub])) for sub in pandigitals]
