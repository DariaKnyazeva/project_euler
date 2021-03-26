"""
LEXICOGRAPHIC PERMUTATIONS
"""
import itertools


if __name__ == "__main__":
    """
    A permutation is an ordered arrangement of objects.
    For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
    If all of the permutations are listed numerically or alphabetically,
    we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits
    0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """
    print("Problem 24: Lexicographic permutations")
    millionth_permutation = list(itertools.permutations(range(10)))[999999]
    print(''.join([str(i) for i in millionth_permutation]))
