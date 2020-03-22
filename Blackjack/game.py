'''
Main game .py
Cointains all the classes
'''

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')

class card:

    def __init__(self, suit :str, rank :str):
        self.suit = suit
        self.rank = rank
        pass

    def __str__(self):
        return self.rank + " of " + self.suit

    pass

class deck:

    def __init__(self):

        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(card(suit,rank))

        pass

    def pick(self, a_card :card):
        return self.cards.pop(self.cards.index(a_card))

    def shuffle(self):
        shuffle(self.cards)
        pass

    pass

class hand:


    pass