"""
DIGIT FACTORIALS
"""
import math

if __name__ == "__main__":
    """
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    Note: As 1! = 1 and 2! = 2 are not sums they are not included.
    """
    print("Problem 34: Digit factorials")
    answer = 0
    for n in range(145, 50000):
        digits = [int(d) for d in str(n)]
        if sum([math.factorial(d) for d in digits]) == n:
            print(n)
            answer += n

    print(answer)
