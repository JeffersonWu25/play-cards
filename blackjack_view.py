"""
View of the Black Jack game
"""

from abc import ABC, abstractmethod

class BlackJackView(ABC):
    """
    Controls view in Black Jack game
    """
    def __init__(self, blackjack_model):
        self.blackjack_model = blackjack_model

    @abstractmethod
    def print_cards(self):
        pass

class BlackJackTextView(BlackJackView):
    """
    Controls view as terminal output
    """
    def print_cards(self):
        your_cards = []
        for card in self.blackjack_model.player_cards:
            your_cards.append(card.number)
        print("--------------------------------------\n"
              f"Dealer cards are: {[self.blackjack_model.dealer_cards[0].number, "X"]} \n"
              f"Your cards are: {your_cards}"
        )

    def output(self):
        player_total = self.blackjack_model.value(self.blackjack_model.player_cards)
        dealer_total = self.blackjack_model.value(self.blackjack_model.dealer_cards)

        your_cards = []
        dealer_cards = []
        for card in self.blackjack_model.player_cards:
            your_cards.append(card.number)
        for card in self.blackjack_model.dealer_cards:
            dealer_cards.append(card.number)

        print("--------------------------------------")
        print(f"You have {your_cards} for a total of {player_total}.")
        print(f"Dealer has {dealer_cards} for a total of {dealer_total}.")

        if player_total > 21:
            print("Player busts. Dealer wins")
        elif dealer_total > 21:
            print(f"Dealer busts. Player wins ${self.blackjack_model.wager}")
        elif player_total > dealer_total:
            print(f"Player wins ${self.blackjack_model.wager}")
        elif dealer_total > player_total:
            print("Dealer wins.")
        else:
            print("Its a push")