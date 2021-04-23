import unittest

from problems.p054 import Card, Hand, Game


class Problem54Test(unittest.TestCase):
    def test_card(self):
        card1 = Card("TS")
        card2 = Card("9S")
        self.assertTrue(card1 > card2)

    def test_hand_high_card(self):
        hand = Hand("8C TS KC 9H 4S 7D 2S 5D 3S AC")
        self.assertEqual(14, hand.high_card())
        hand = Hand("2C 5C 7D 8S QH")
        self.assertEqual(12, hand.high_card())

    def test_hand_one_pair(self):
        hand = Hand("QD AS 6H JS 2C")
        self.assertEqual(0, hand.pair())
        hand = Hand("2C 5C QD QH")
        self.assertEqual(12, hand.pair())

    def test_hand_two_pairs(self):
        hand = Hand("QD QH 2C 2H")
        self.assertEqual(12, hand.two_pairs())

        hand = Hand("2C 2H 2D 2S")
        self.assertEqual(2, hand.two_pairs())

    def test_hand_three_of_a_kind(self):
        hand = Hand("2C 2H QD QH")
        self.assertEqual(0, hand.three_of_a_kind())
        hand = Hand("2C 2H 2D QH")
        self.assertEqual(2, hand.three_of_a_kind())

    def test_hand_straight(self):
        hand = Hand("2C 2H QD QH")
        self.assertEqual(0, hand.straight())

        hand = Hand("2C 3H 4D 5H")
        self.assertEqual(5, hand.straight())

    def test_hand_flush(self):
        hand = Hand("2C 2H QD QH")
        self.assertFalse(hand.flush())

        hand = Hand("2C 3C QC KC")
        self.assertTrue(hand.flush())

    def test_hand_full_house(self):
        hand = Hand("2C 2H QD QH AC")
        self.assertFalse(hand.full_house())

        hand = Hand("2C 2H 2S KC KH")
        self.assertTrue(hand.full_house())

        hand = Hand("2C 2H 2S 2D KH")
        self.assertFalse(hand.full_house())

    def test_hand_four_of_a_kind(self):
        hand = Hand("2C 2H QD QH AC")
        self.assertFalse(hand.four_of_a_kind())

        hand = Hand("2C 2H 2D 2S AC")
        self.assertEqual(2, hand.four_of_a_kind())

    def test_hand_straigt_flush(self):
        hand = Hand("2C 3C 4C 5C 6C")
        self.assertTrue(hand.straight_flush())

        hand = Hand("2C 3C 4C 5C TC")
        self.assertFalse(hand.straight_flush())

        hand = Hand("2C 3C 4C 5C 6S")
        self.assertFalse(hand.straight_flush())

    def test_hand_royal_flush(self):
        hand = Hand("2C 2H QD QH AC")
        self.assertFalse(hand.royal_flush())

        hand = Hand("TC JC QC KC AC")
        self.assertTrue(hand.royal_flush())

        hand = Hand("TC JC QC KC AD")
        self.assertFalse(hand.royal_flush())

    def test_game_win_with_pair(self):
        """
        Checking the scenario

        Player 1        Player 2                Winner
1       5H 5C 6S 7S KD    2C 3S 8S 8D TD        Player 2
         Pair of Fives     Pair of Eights
        """
        game = Game("5H 5C 6S 7S KD 2C 3S 8S 8D TD")
        self.assertEqual("5H 5C 6S 7S KD", str(game.hand1))
        self.assertEqual("2C 3S 8S 8D TD", str(game.hand2))
        self.assertEqual(0, game.win())

    def test_game_win_with_highest_card(self):
        """
        Testing the scenario Player 1 wins with Highest card
        5D 8C 9S JS AC    2C 5C 7D 8S QH
        Highest card Ace  Highest card Queen
        """
        game = Game("5D 8C 9S JS AC 2C 5C 7D 8S QH")
        self.assertEqual(1, game.win())

    def test_game_win(self):
        game = Game("2D 9C AS AH AC 3D 6D 7D TD QD")
        self.assertEqual(0, game.win())

        game = Game("4D 6S 9H QH QC 3D 6D 7H QD QS")
        self.assertEqual(1, game.win())

        game = Game("2H 2D 4C 4D 4S 3C 3D 3S 9S 9D")
        self.assertEqual(1, game.win())


unittest.main()
