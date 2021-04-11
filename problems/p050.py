# CONSEQUETIVE PRIME SUM

"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes
that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand
that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum
of the most consecutive primes?
"""

from utils.prime_numbers import primes


if __name__ == "__main__":
    print(__doc__)
    print("*" * 60)

    prime_numbers = list(primes(1000000))
    max_len = 0
    answer = 0

    for i in range(10):
        for j in range(i + 2, len(prime_numbers)):
            consequetive = prime_numbers[i:j]
            n = sum(consequetive)
            if n > 1000000:
                break
            if n in prime_numbers:
                if len(consequetive) > max_len:
                    max_len = len(consequetive)
                    answer = n

    print(answer)
