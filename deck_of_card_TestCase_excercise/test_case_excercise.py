from deck_of_card_excercise import Card,Deck
import unittest

class Test_Case_excersice(unittest.TestCase):
    def setUp(self):
        self.deck_of_card_TestCase_excercise.deck_of_card_excercise=Card("Hearts","2")
    def test_init(self):
        self.assertEqual(self.deck_of_card_TestCase_excercise.deck_of_card_excercise.suit, "Hearts")
        self.assertEqual(self.deck_of_card_TestCase_excercise.deck_of_card_excercise.value, "2")
    def test_repr(self):
        self.assertEqual(repr(self.deck_of_card_TestCase_excercise.deck_of_card_excercise.Card), "2 of Hearts")
if __name__ == "__main__":
    Test_Case_excersice.main()