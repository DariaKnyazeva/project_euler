# DIGIT CANCELLING FRACTIONS

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

if __name__ == "__main__":
    print(__doc__)
    print("*" * 60)
    numerators = []
    denominators = []
    for x in range(11, 100):
        if x % 10 == 0:  # skip trivial fractions
            continue
        for y in range(x + 1, 100):
            if y % 10 == 0:  # skip trivial fractions
                continue
            numerator = str(x)
            denominator = str(y)
            if numerator[0] not in denominator and numerator[1] not in denominator:
                continue
            if numerator[0] in denominator:
                denominator = int(denominator.replace(numerator[0], '', 1))
                numerator = int(numerator[1])
            elif numerator[1] in denominator:
                denominator = int(denominator.replace(numerator[1], '', 1))
                numerator = int(numerator[0])
            if numerator / denominator == x / y:
                numerators.append(numerator)
                denominators.append(denominator)
                print(f"{x}/{y}: {numerator}/{denominator}")

    # Now that we find all 4 fractions, have to simplify their product
    for divisor in range(2, 10):
        can_simplify_num = [x for x in numerators if x % divisor == 0]
        can_simplify_denom = [x for x in denominators if x % divisor == 0]
        if len(can_simplify_num) > 0 and len(can_simplify_denom) > 0:
            numerators[numerators.index(can_simplify_num[0])] //= divisor
            denominators[denominators.index(can_simplify_denom[0])] //= divisor
    print(f"Answer {denominators[0]*denominators[1]*denominators[2]*denominators[3]}")
