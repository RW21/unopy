import time

from deck import Deck
from game import Game
from player import Player


def bot_play():
    p1 = Player('bot', 'dare')
    p2 = Player('bot', 'robot')
    deck = Deck()
    bot_game = Game(deck, [p1, p2])

    bot_game.distribute(7)

    while bot_game.current_cards():
        bot_game.play()

        if len(bot_game.deck) == 0:
            break
        print(bot_game.state)
        print(bot_game.field)
        print(bot_game.wildcard)
        time.sleep(0.15)

    print('end')

bot_play()