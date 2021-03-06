# 1000-DIGIT FIBONACCI NUMBER

"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence
to contain 1000 digits?
"""


def fibonacci(limit):
    a, b = 1, 1
    while a < limit:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print(__doc__)
    print("*" * 65)
    fibos = fibonacci(int('9' * 1000))
    for idx, n in enumerate(fibos):
        if n > int('9' * 999):
            print(idx + 1)
            break
