"""
LONGEST COLLATZ SEQUENCE
"""
import unittest


def collatz_sequence(start_number):
    """
    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem), it is thought
    that all starting numbers finish at 1.
    """
    yield start_number
    while start_number != 1:
        if start_number % 2 == 0:
            start_number = start_number // 2
        else:
            start_number = 3 * start_number + 1
        yield start_number
        collatz_sequence(start_number)


def longest_collatz_sequence(limit=1000000):
    """
    Which starting number, under one million, produces the longest chain of the Collatz sequence?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """
    max = 1
    for i in range(limit, 1, -1):
        seq_len = len(list(collatz_sequence(i)))
        if seq_len > max:
            max = seq_len
            print("{} seq is of lentgh {}".format(i, seq_len))


class Problem14Test(unittest.TestCase):
    def test_collatz_sequence(self):
        self.assertEqual(list(collatz_sequence(13)),
                         [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])


# unittest.main()


if __name__ == "__main__":
    print("Problem 14: Longest Collatz sequence")
    longest_collatz_sequence(1000000)
