# POKER HANDS

"""
In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank
made up of the highest value wins; for example, a pair of eights
beats a pair of fives (see example 1 below).

But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:


Hand        Player 1        Player 2            Winner
1       5H 5C 6S 7S KD    2C 3S 8S 8D TD        Player 2
         Pair of Fives     Pair of Eights

2       5D 8C 9S JS AC    2C 5C 7D 8S QH        Player 1
        Highest card Ace  Highest card Queen

3       2D 9C AS AH AC    3D 6D 7D TD QD        Player 2
        Three Aces        Flush with Diamonds

4       4D 6S 9H QH QC     3D 6D 7H QD QS        Player 1
        Pair of Queens     Pair of Queens
        Highest card Nine  Highest card Seven

5       2H 2D 4C 4D 4S     3C 3D 3S 9S 9D        Player 1
        Full House         Full House
        With Three Fours   With Three Threes

The file, data/p054_poker.txt, contains one-thousand random hands
dealt to two players. Each line of the file contains ten cards
(separated by a single space): the first five are Player 1's cards
and the last five are Player 2's cards. You can assume that all hands
are valid (no invalid characters or repeated cards),
each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?
"""


class Card:
    RANKS = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    SUITS = ['D', 'H', 'C', 'S']

    def __init__(self, card_str):
        """
        @param card_str is a string representation of a card,
        where the last char is the suit
        for example 8C TS KC 9H 4S 7D 2S 5D 3S AC
        """
        assert len(card_str) == 2
        card_str = card_str.upper()
        assert card_str[0] in self.RANKS
        assert card_str[-1] in self.SUITS

        self.rank = card_str[0]
        self.suit = card_str[-1]

    def __str__(self):
        return f"{self.rank}{self.suit}"

    @classmethod
    def rank_name(cls, rank):
        if int(rank) <= 10:
            return str(rank)
        ranks = {
            11: "Jack",
            12: "Queen",
            13: "King",
            14: "Ace",
        }
        return ranks[rank]

    @property
    def value(self):
        return self.RANKS[self.rank]

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


class HandRank:
    HAND_RANKS = {
        10: "Royal Flush",
        9: "Straight Flush",
        8: "Four of a Kind",
        7: "Full House",
        6: "Flush",
        5: "Straight",
        4: "Three of a Kind",
        3: "Two Pairs",
        2: "Pair",
        1: "High Card",
    }

    def __init__(self, rank, high_card):
        self.rank = rank
        self.name = self.HAND_RANKS[rank]
        self.high_card = high_card

    def __str__(self):
        return f'{self.name} of {Card.rank_name(self.high_card)}'

    def __eq__(self, other):
        return self.rank == other.rank and self.high_card == other.high_card

    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        elif self.rank == other.rank:
            return self.high_card < other.high_card
        else:
            return False

    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        elif self.rank == other.rank:
            return self.high_card > other.high_card
        else:
            return False


class Hand:

    def __init__(self, cards_str):
        self.cards = [Card(card) for card in cards_str.split(" ")]
        self.ranks = [
            HandRank(10, self.royal_flush()),
            HandRank(9, self.straight_flush()),
            HandRank(8, self.four_of_a_kind()),
            HandRank(7, self.full_house()),
            HandRank(6, self.flush()),
            HandRank(5, self.straight()),
            HandRank(4, self.three_of_a_kind()),
            HandRank(3, self.two_pairs()),
            HandRank(2, self.pair()),
            HandRank(1, self.high_card()),
        ]

    def __str__(self):
        return " ".join(str(card) for card in self.cards)

    def highest_value_except_rank(self, rank):
        except_cards = rank.high_card
        values = [card.value for card in self.cards if card.value != except_cards]
        return sorted(values, reverse=True)[0]

    def high_card(self):
        """
        Highest value card
        """
        return max(self.cards).value

    def pair(self):
        values = sorted([card.value for card in self.cards])
        pairs = []
        for val in values:
            if values.count(val) > 1:
                pairs.append(val)
        if len(pairs) == 2:
            return pairs[0]
        return 0

    def two_pairs(self):
        values = sorted([card.value for card in self.cards])
        pairs = []
        for val in values:
            if values.count(val) > 1:
                pairs.append(val)
        if len(pairs) == 4:
            return pairs[-1]
        return 0

    def three_of_a_kind(self):
        """
        Three cards of the same value.
        """
        values = [card.value for card in self.cards]
        for val in values:
            if values.count(val) == 3:
                return val
        return 0

    def straight(self):
        """
        All cards are consecutive values
        """
        values = [card.value for card in self.cards]
        values = sorted(values)
        for idx in range(len(values) - 1, 0, -1):
            if values[idx] - values[idx - 1] != 1:
                return 0
        return values[-1]

    def flush(self):
        """
        All cards of the same suit.
        """
        suits = set([card.suit for card in self.cards])
        if len(suits) == 1:
            return self.high_card()
        return 0

    def full_house(self):
        """
        Three of a kind and a pair
        """
        values = [card.value for card in self.cards]
        if len(set(values)) == 2:
            for val in values:
                if values.count(val) == 3:
                    return val
        return 0

    def four_of_a_kind(self):
        """
        Four cards of the same value
        """
        values = [card.value for card in self.cards]
        for val in values:
            if values.count(val) == 4:
                return val
        return 0

    def straight_flush(self):
        """
        All cards are consecutive values of same suit
        """
        if self.flush():
            return self.straight()
        return 0

    def royal_flush(self):
        """
        Royal Flush: Ten, Jack, Queen, King, Ace, in same suit
        """
        if self.flush():
            values = [card.value for card in self.cards]
            sorted(values)
            if values == [10, 11, 12, 13, 14]:
                return 14
        return 0


class Game:
    def __init__(self, game_str):
        game_str = game_str.strip()
        assert game_str
        self.hand1 = Hand(game_str[:15].strip())
        self.hand2 = Hand(game_str[15:].strip())

    def win(self, verbose=False):
        winner = self.get_winner(verbose=verbose)
        if winner == self.hand1:
            return 1
        return 0

    def get_winner(self, verbose=False):
        # import ipdb; ipdb.set_trace()
        if verbose:
            print(f"{self.hand1}  VS  {self.hand2}")
        rank1 = self.hand1.ranks
        rank2 = self.hand2.ranks
        for index, rank in enumerate(rank1):
            if rank > rank2[index]:
                if verbose:
                    print(f"Player 1 win with {rank}")
                return self.hand1
            elif rank < rank2[index]:
                if verbose:
                    print(f"Player 2 win with {rank2[index]}")
                return self.hand2
            elif rank.high_card in [0, 1]:
                continue
            else:
                if verbose:
                    print(f"Both players have {rank}")
                high_card_1 = self.hand1.highest_value_except_rank(rank)
                high_card_2 = self.hand2.highest_value_except_rank(rank)
                if high_card_1 > high_card_2:
                    if verbose:
                        print(f"Player 1 win with {Card.rank_name(high_card_1)}")
                    return self.hand1
                elif high_card_1 < high_card_2:
                    if verbose:
                        print(f"Player 2 win with {Card.rank_name(high_card_2)}")
                    return self.hand2
                else:
                    continue


if __name__ == "__main__":
    print(__doc__)
    print("*" * 60)

    answer = 0
    with open("data/p054_poker.txt", "r") as f:
        for game_str in f.readlines():
            answer += Game(game_str).win(verbose=True)

    print(answer)
