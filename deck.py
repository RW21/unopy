from random import shuffle


class Deck:
    """
    There are four suits, Red, Green, Yellow and Blue, each consisting of one 0 card, two 1 cards, two 2s, 3s, 4s, 5s, 6s, 7s, 8s and 9s; two Draw Two cards;
     two Skip cards; and two Reverse cards. In addition there are four Wild cards and four Wild Draw Four cards.

     http://play-k.kaserver5.org/Uno.html

"""
    colors = 'yellow green red blue'.split()
    number = [str(n) for n in range(2) for n in (list(range(1,10)) + list('DRS'))]
    special = [n for n in range(4) for n in ['W','w']]

    def __init__(self):
        self.cards  = [(color, number) for color in self.colors
                                        for number in self.number]\
                      + [('', number) for number in self.special]\
                      + [(color, '0') for color in self.colors]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

    def __repr__(self):
        return str(self.cards)

    def draw(self):
        return self.cards.pop(len(self.cards)-1)

    def shuffle(self):
        shuffle(self.cards)
