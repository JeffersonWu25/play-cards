"""
Card deck that will be used for all card game
"""

import random

SUIT_VALUES = ["Spade", "Clover", "Heart", "Diamond"]
NUMBER_VALUES = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

class Deck:
    """
    Representation of a card deck
    """

    def __init__(self):
        self.next_card = 0
        self.deck = []
        for suit in SUIT_VALUES:
            for number in NUMBER_VALUES:
                self.deck.append(Card(suit, number))

    def shuffle_deck(self):
        """
        shuffles the deck
        """
        random.shuffle(self.deck)
        return self.deck
    
    def select_top_card(self):
        """
        selects card on the top of the deck
        """
        try:
            top_card = self.deck[self.next_card]
            self.next_card += 1
            return top_card
        except IndexError:
            print("Reached end of deck")

    def __repr__(self):
        return f"{self.deck}"
    
class Card:
    """
    Card in a deck
    """

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return f"({self.suit}, {self.number})"
    
deck = Deck()
print(deck)