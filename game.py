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

        while self.field == ('','w') or self.field == ('', 'W'):
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

        elif self.wildcard != '':
            self.field = self.current_cards().pop(index)


        else:
            return False

    def new_turn(self):
        if self.field[1] == 'R':
            self.reverse = not self.reverse

        elif self.reverse:
            self.turn = self.turn - 1

        elif self.field[1] == 'S':
            self.turn = self.turn +2

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

        elif not wildcard and not is_card(self.current_cards(), self.field):
            for index, card in enumerate(self.current_cards()):
                if card == ('', 'w') or card == ('','W'):
                    self.send(index)
                    self.wildcard = bot_select_color_wild(self.current_cards(), maxmin ='min')


        elif not is_card(self.current_cards(), self.field) and not wildcard:
            self.current_cards().append(self.deck.draw())
            print('drawed')

        if wildcard:
            if is_card(self.current_cards(), (self.wildcard, '')):
                if self.current_player.type == 'bot':
                    # return false when there is no card
                    card_status = send_card_with_color(self.current_cards(), self.wildcard)
                    if card_status:
                        self.send(card_status)
                    elif not card_status:
                        for index, card in self.current_cards():
                            if card == ('', 'w') or card == ('','W'):
                                self.send(index)
                    else:
                        self.current_cards().append(self.deck.draw())


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
                self.wildcard = bot_select_color_wild(self.current_cards(), maxmin='min')

            if self.current_player.type == 'human':
                self.wildcard = user_input_which_color(self.current_cards())

        if self.field == ('W', ''):
            self.draw_damage = 4

        if len(self.deck.cards) == 0:
            return False

        self.new_turn()

