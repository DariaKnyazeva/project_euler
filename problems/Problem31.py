"""
COIN SUMS
"""


if __name__ == "__main__":
    """
    In the United Kingdom the currency is made up of pound (£) and pence (p).
    There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
    It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?
    """
    print("Problem 31: Coin sums")

    number_of_coins = 7
    # I do not consider £2 coin, as it is the only variant
    pounds = 201
    coins = [1, 2, 5, 10, 20, 50, 100]

    s = "0 " * pounds
    # create number_of_coins X pounds zero matrix
    T = [[int(digit) for digit in s.strip().split(" ")] for i in range(number_of_coins)]

    for i in range(number_of_coins):
        for j in range(pounds):
            T[i][0] = 1
            T[0][j] = 1
    # the 1st row and the 1st column of matrix are now all "1"s

    for i in range(1, number_of_coins):
        for j in range(pounds):
            if j < coins[i]:
                T[i][j] = T[i - 1][j]
            else:  # the new type of coin is introduced
                T[i][j] = T[i - 1][j] + T[i][j - coins[i]]

    # The right bottom corner of the matrix has the anser.
    # Have to add 1 for the 200p coin.
    print(T[-1][-1] + 1)
