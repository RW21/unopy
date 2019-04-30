from unittest import TestCase

from deck import Deck
from game import Game
from player import Player

p1 = Player('bot', 'dare')
p2 = Player('bot', 'robot')

deck = Deck()

a = Game(deck, [p1, p2])
# a.distribute()



class TestGame(TestCase):
    def test_play_last(self):
        a.state = {p1: [('red', '8')], p2: [('red', 'D')]}
        a.current_player = p1
        a.field = ('red', '8')
        a.play()

        assert a.state == {p1: [], p2: [('red', 'D')]}

    def test_play_general(self):
        a.state = {p1: [('green', 'R'), ('green', '4'), ('yellow', '8'), ('red', 'R'), ('red', '1')],
                   p2: [('yellow', '7'), ('red', 'R'), ('yellow', '5'), ('yellow', '3'), ('green', '3'),
                        ('yellow', '4'), ('green', '6')]}
        a.field = ('yellow', '1')
        a.current_player = p1
        a.play()

        print(a.state)

        assert a.state == {p1: [('green', 'R'), ('green', '4'), ('red', 'R'), ('red', '1')],
                           p2: [('yellow', '7'), ('red', 'R'), ('yellow', '5'), ('yellow', '3'), ('green', '3'),
                                ('yellow', '4'), ('green', '6')]}

    def test_bot_when_wild(self):
        """
        Checks behaviour of bot when wild and player currently possess the card.
        """
        a.state = {p1: [('green', 'R'), ('green', '4')],
                   p2: [('yellow', '7'), ('red', 'R'), ('yellow', '5')]}
        a.field = ('', 'w')
        a.wildcard = 'red'
        a.current_player = p2

        a.play()

        print(a.state)

        assert a.state == {p1: [('green', 'R'), ('green', '4')],
                           p2: [('yellow', '7'), ('yellow', '5')]}

    # def test_bot_when_wild(self):
