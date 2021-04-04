"""
TRUNCATABLE PRIMES
"""
from utils.prime_numbers import primes


if __name__ == "__main__":
    """
    The number 3797 has an interesting property. Being prime itself,
    it is possible to continuously remove digits from left to right,
    and remain prime at each stage: 3797, 797, 97, and 7.
    Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable
    from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    """
    print("Problem 37: Truncatable primes")
    all_prime_numbers = list(primes(739398))
    prime_numbers = all_prime_numbers[8:]
    answer = 0
    for n in prime_numbers:
        n = str(n)
        truncatable = True
        for i in range(len(n)):
            if int(n[i:]) not in all_prime_numbers:
                truncatable = False
                break
            if not n[:i]:
                continue
            if int(n[:i]) not in all_prime_numbers:
                truncatable = False
                break
        if truncatable:
            print(n)
            answer += int(n)
    print(f" Answer is {answer}")
