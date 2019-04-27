from unittest import TestCase
from game_helper import is_card, is_sendable

card1 = ('blue', '7')
card2 = ('red', '7')
card3 = ('blue', '1')
card4 = ('green', '3')

deck = [('blue', '7'),('blue', '7'),('yellow', '2')]


class TestIs_sendable(TestCase):


    def test_number(self):
        assert is_sendable(card1,card2)

    def test_color(self):
        assert is_sendable(card1,card3)

        assert not is_sendable(card2, card3)

class Test_is_card(TestCase):

    def test_is_card(self):
        assert is_card(deck, card3)
        assert not is_card(deck, card4)






