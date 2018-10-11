# Milestone Project 2
# Multiplayer blackjack game


from __future__ import print_function
import random


class Deck(object):
    def __init__(self, deck_cards):
        self.deck_card = deck_cards

    def card_value(self):
        return random.choice(self.deck_card)


class Players(object):
    def __init__(self, name, bankroll):
        self.name = name
        self.bankroll = bankroll

    def add_bankroll(self, winnings):
        self.bankroll += winnings

    def sub_bankroll(self, loss):
        self.bankroll -= loss


cards = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J')
dealer = Deck(cards)
print(cards)
print(dealer.card_value())
