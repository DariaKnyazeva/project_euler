# COMBINATORIC SELECTIONS


"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (5 3) = 10


In general, (n r) = n! / r!(n - r)!

where r <= n, n! = n*(n-1)*...*3*2*1, and 0! = 1.

It is not until 23, that a value exceeds one-million:
(23 10) = 1144066.

How many, not necessarily distinct, values of (n r)
for 1 <= n <= 100 are greater than one-million?
"""


from utils.combinatorics import c_n_k


if __name__ == "__main__":
    print(__doc__)
    print("*" * 55)

    answer = 0

    for n in range(1, 101):
        for k in range(1, n + 1):
            if c_n_k(n, k) > 1000000:
                answer += 1
    print(answer)
