from collections import Counter
from pprint import pprint
from game_helper import *
from random import randint


def sendables(cards, field):
    return [i for i in cards if is_sendable(i,field)]


def user_input(cards):
    pprint(cards)
    index = input('Which card?')

    return int(index)

def user_input_which_color(cards):
    pprint(cards)
    return input('What color?')


def bot_play(cards, field):
    return randint(0, len(sendables(cards, field)) - 1)

def bot_select_color_wild(cards, field, maxmin = 'max'):
    color_count = Counter([color[0] for color in cards])



    if maxmin == 'max':
        max_number = 0
        for k, v in color_count.items():
            if v > max_number:
                max_number = v
                max_color = k

        return max_color

    if maxmin == 'min':
        min_number = 1000
        for k, v in color_count.items():
            if v < min_number:
                min_number = v
                min_color = k

        return min_color

def send_card_with_color(cards, color):

    for index, card in enumerate(cards):
        if card[0] == color:
            return index

    return False





class Player:

    def __init__(self, type, name):
        if type == 'bot' or type == 'human':
            self.type = type
        else:
            self.type = ''

        self.name = name
        self.point = 0


    def __repr__(self):
        return self.name + ' ' + self.type
