import time
from random import choice

from deck import Deck
from player import *


class Game:

    def __init__(self, deck: Deck, players):
        self.state: dict
        self.current_player: Player

        self.players = players

        self.state = self.generate_players()
        self.deck = deck

        self.deck.shuffle()

        self.turn = 0
        self.count = 0
        self.field = self.deck.draw()
        self.current_player = choice(players)

        self.reverse = False
        self.wildcard = ''

        self.draw_damage = 0

    def __len__(self):
        return self.count

    def distribute(self, number):
        self.deck.shuffle()
        for i in range(number):
            for j in self.players:
                self.state.get(j).append(self.deck.draw())

    def generate_players(self):
        return {player: [] for player in self.players}

    def current_cards(self):
        return self.state.get(self.current_player)

    def send(self, index):
        if is_sendable(self.current_cards()[index], self.field):
            self.field = self.current_cards().pop(index)
            return True

        else:
            return False

    def new_turn(self):
        if self.field[1] == 'R':
            self.reverse = not self.reverse

        if self.reverse:
            self.turn = self.turn - 1

        else:
            self.turn = self.turn + 1

        self.current_player = list(self.state.keys())[self.turn % len(self.players) - 1]
        self.count = self.count + 1

    def place_card(self, wildcard=False):
        # sends card
        if is_card(self.current_cards(), self.field) and not wildcard:
            if self.current_player.type == 'bot':
                self.send(bot_play(self.current_cards(), self.field))

            if self.current_player.type == 'human':

                index = user_input(self.current_cards())

                # send returns false if not sendable
                if not self.send(index):
                    while not self.send(index):
                        print(self.field)
                        index = user_input(self.current_cards())

        elif not is_card(self.current_cards(), self.field) and not wildcard:
            self.current_cards().append(self.deck.draw())
            print('drawed')

        if wildcard:
            if is_card(self.current_cards(), (self.wildcard, '')):
                if self.current_player.type == 'bot':
                    if not send_card_with_color(self.current_cards(),
                                                bot_select_color_wild(self.current_cards(), self.wildcard)):
                        self.current_cards().append(self.deck.draw())
                        print('no cards -> draws')

                if self.current_player.type == 'human':
                    if is_card(self.current_cards(), self.field):
                        self.current_cards().append(self.deck.draw())
                        print('no cards -> draws')
                    else:

                        index = user_input(self.current_cards())

                        # send returns false if not sendable
                        if not self.send(index):
                            while not self.send(index):
                                print(self.field)
                                index = user_input(self.current_cards())

    def play(self):

        # process draw
        if self.draw_damage != 0:

            for cards in range(self.draw_damage):
                self.current_cards().append(self.deck.draw())

            self.draw_damage = 0

        # process wild card
        if self.wildcard != '':
            self.place_card(wildcard=True)

        else:
            self.place_card()


        self.wildcard = ''

        # if wild card is placed
        if self.field == ('w', '') or self.field == ('W', ''):
            if self.current_player.type == 'bot':
                self.wildcard = bot_select_color_wild(self.current_cards(), self.field, maxmin='min')

            if self.current_player.type == 'human':
                self.wildcard = user_input_which_color(self.current_cards())

        if self.field == ('W', ''):
            self.draw_damage = 4

        self.new_turn()


p1 = Player('bot', 'dare')
p2 = Player('bot', 'robot')

b = Deck()
print(b)
a = Game(b, [p1, p2])
print(a.state)
a.distribute(7)
print(a.state)

print('now:' + str(a.current_player))
print(a.field)

while len(a.deck) >= 0:
    print(a.current_player)
    print(a.state)
    print(a.field)
    a.play()
    # time.sleep(1)
