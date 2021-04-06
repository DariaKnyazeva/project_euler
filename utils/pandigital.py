import itertools


def is_pandigital(n, limit=9):
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


def pandigitats(n_digits):
    """
    Returns list of n-digit pandigital numbers ordered lexicographically
    """
    pandigitals = itertools.permutations(range(1, n_digits))
    pandigitals = [int("".join([str(i) for i in sub])) for sub in pandigitals]
    return pandigitals
