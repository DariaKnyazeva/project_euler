# POWERFUL DIGIT SUM

"""
A googol (10^100) is a massive number:
one followed by one-hundred zeros;
100^100 is almost unimaginably large:
one followed by two-hundred zeros.
Despite their size, the sum of the digits
in each number is only 1.

Considering natural numbers of the form,
a^b, where a, b < 100, what is the maximum digital sum?
"""

import asyncio


async def digits_sum(n):
    return sum(int(digit) for digit in str(n))


async def main():
    max_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            c = await digits_sum(a**b)
            if c > max_sum:
                max_sum = c
    return max_sum


if __name__ == "__main__":
    print(__doc__)
    print("*" * 55)

    res = asyncio.run(main())
    print(res)
