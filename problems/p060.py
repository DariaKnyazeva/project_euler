# PRIME PAIR SETS

"""
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in
any order the result will always be prime. For example,
taking 7 and 109, both 7109 and 1097 are prime. The sum
of these four primes, 792, represents the lowest sum for
a set of four primes with this property.

Find the lowest sum for a set of five primes for which
any two primes concatenate to produce another prime.
"""
import sys

from utils.prime_numbers import primes, is_prime


def check_primes(primes=None):
    if primes is None:
        primes = []
    for i in range(len(primes) - 1):
        if not is_prime(int(f"{primes[i]}{primes[-1]}")):
            return False
        if not is_prime(int(f"{primes[-1]}{primes[i]}")):
            return False
    return True


if __name__ == "__main__":
    print(__doc__)
    print("*" * 55)

    prime_numbers = list(primes(30000))
    prime_numbers.remove(2)  # ends with 2 is not a prime number
    prime_numbers.remove(5)  # ends with 5 is not a prime number

    total = len(prime_numbers)

    for idx, prime in enumerate(prime_numbers):
        # prime_list = [prime, ]
        print(prime)
        if prime * 5 > prime_numbers[-1]:
            break
        for j in range(idx + 1, total):
            prime2 = prime_numbers[j]
            print(f"--{prime2}")
            if prime2 * 4 > prime_numbers[-1]:
                break
            if check_primes([prime, prime2]):
                for k in range(j + 1, total):
                    prime3 = prime_numbers[k]
                    if check_primes([prime, prime2, prime3]):
                        for ll in range(k + 1, total):
                            prime4 = prime_numbers[ll]
                            if check_primes([prime, prime2, prime3, prime4]):
                                for m in range(ll + 1, total):
                                    prime5 = prime_numbers[m]
                                    prime_list = [prime, prime2, prime3, prime4, prime5, ]
                                    if check_primes(prime_list):
                                        print(prime_list)
                                        answer = sum(prime_list)
                                        print(answer)
                                        if answer < prime_numbers[-1]:
                                            sys.exit()
                                    else:
                                        continue
                            else:
                                continue
                    else:
                        continue
            else:
                continue
