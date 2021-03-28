"""
RECIPROCAL CYCLES
"""
import re


def decimal_repr(numerator, denuminator, min_cycle_len=1):
    zeros = ""
    while numerator < denuminator:
        numerator *= 10
        zeros += "0"
    zeros = zeros[1:]

    result = f"0.{zeros}{numerator//denuminator}"
    cycle_len = 0
    while numerator % denuminator != 0 and cycle_len < 1500:
        zeros = ""
        numerator = numerator - denuminator * (numerator // denuminator)
        while numerator < denuminator:
            numerator *= 10
            zeros += "0"
        zeros = zeros[1:]
        result = f"{result}{zeros}{numerator//denuminator}"
        cycle_len += 1

    return format_cyclic_fraction(result, min_cycle_len=min_cycle_len)


def format_cyclic_fraction(fraction, min_cycle_len=1):
    min_cycle_len = min_cycle_len
    fraction = fraction.replace("0.", "")
    cycle = ""

    for digit_idx, digit in enumerate(fraction):
        sub = fraction[digit_idx: digit_idx + min_cycle_len]
        positions = [i.start() for i in re.finditer(sub, fraction)]
        if len(positions) == 1:
            continue
        if positions[1] - positions[0] < min_cycle_len:
            continue
        is_cycle = True
        try:
            for i in range(positions[1] - positions[0]):
                if fraction[positions[0] + i] != fraction[positions[1] + i]:
                    is_cycle = False
                    continue
        except IndexError:
            is_cycle = False
            continue
        if is_cycle:
            cycle = fraction[positions[0]: positions[1]]
            fraction = fraction[0: fraction.find(cycle)]
            break

    if cycle:
        return f"0.{fraction}({cycle})"
    return f"0.{fraction}"


if __name__ == "__main__":
    """
    A unit fraction contains 1 in the numerator.
    The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2 =   0.5
    1/3 =   0.(3)
    1/4 =   0.25
    1/5 =   0.2
    1/6 =   0.1(6)
    1/7 =   0.(142857)
    1/8 =   0.125
    1/9 =   0.(1)
    1/10    =   0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
    It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle
    in its decimal fraction part.
    """
    print("Problem 26: Reciprocal cycles")
    max_cycle = 0
    answer = 7
    for n in range(43, 998):
        fraction = decimal_repr(1, n, min_cycle_len=10)
        if "(" in fraction:
            cycle = fraction[fraction.find("(") + 1: fraction.find(")")]
            if len(cycle) > max_cycle:
                max_cycle = len(cycle)
                answer = n
    print(f"{answer}: the length of cycle is {max_cycle}")
