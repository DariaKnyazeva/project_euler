# CODED TRIANGLE NUMBERS

"""
The nth term of the sequence of triangle numbers is given by,
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number
corresponding to its alphabetical position and
adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall
call the word a triangle word.

Using data/p042_words.txt, a 16K text file containing nearly
two-thousand common English words, how many are triangle words?
"""


def triangulars(size):
    for n in range(1, size + 1):
        yield int(0.5 * n * (n + 1))


def letter_to_int(letter):
    return ord(letter) - 64


def word_to_number(word):
    return sum(letter_to_int(letter) for letter in word)


if __name__ == "__main__":
    print(__doc__)
    print("*" * 55)
    triangulars = list(triangulars(1000))
    with open('data/p042_words.txt', 'r') as f:
        words = f.readlines()[0]
        words = words.replace('"', "").split(",")
        triangular_words = [w for w in words if word_to_number(w) in triangulars]
        print(len(triangular_words))
