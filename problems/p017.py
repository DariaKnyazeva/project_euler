# NUMBER LETTER COUNTS

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342
(three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance
with British usage.
"""


words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

if __name__ == "__main__":
    print(__doc__)

    all_words = []
    for number in range(1, 20):
        all_words.append(words[number])
    for number in range(20, 100):
        if number % 10 == 0:
            all_words.append(words[number])
        else:
            all_words.append("{} {}".format(words[(number // 10) * 10],
                                            words[int(str(number)[-1])]))
    for number in range(100, 1000):
        hundreds = words[int(str(number)[0])]
        if number % 100 == 0:
            all_words.append("{} hundred".format(hundreds))
        elif number % 10 == 0:
            tens = words[int(str(number)[1:])]
            all_words.append("{} hundred and {}".format(hundreds, tens))
        else:
            if int(str(number)[1:]) < 20:
                tens = ''
                if str(number)[1] == '0':
                    ones = words[int(str(number)[-1])]
                else:
                    ones = words[int(str(number)[1:])]
            else:
                tens = words[int(str(number)[1:]) // 10 * 10]
                ones = words[int(str(number)[-1])]
            all_words.append("{} hundred and {} {}".format(hundreds, tens, ones))

    all_words.append("one thousand")
    all_words = "".join(all_words).replace(" ", "")
    print("*" * 60)
    print(len(all_words))
