"""
controls user imput for blackjack game
"""

from abc import ABC, abstractmethod

class BlackJackController(ABC):
    """
    Controls user interactions in Black Jack game
    """
    def __init__(self, blackjack_model):
        self.blackjack_model = blackjack_model

    @abstractmethod
    def wager(self):
        pass

class BlackJackTextController(BlackJackController):
    """
    Controls user interactions by text inputs
    """

    def wager(self):
        wager_amount = int(input(f"How much would you like to wager? You have ${self.blackjack_model.money}. "))
        if wager_amount <= self.blackjack_model.money:
            self.blackjack_model.set_wager(wager_amount)
        else:
            print("You do not have enough money to place that bet")
            self.wager()

    def move(self):
        options = []
        if self.blackjack_model.check_if_can_hit(self.blackjack_model.player_cards):
            options.append("hit")
        if self.blackjack_model.check_if_can_split(self.blackjack_model.player_cards):
            options.append("split")
        if self.blackjack_model.check_if_can_double_down(self.blackjack_model.player_cards):
            options.append("double down")
        options.append("stay")
        choice = input(f"What would you like to do? ({"/".join(options)}) ")

        if choice in options and choice == "hit":
            self.blackjack_model.hit(self.blackjack_model.player_cards)
        elif choice == "stay":
            self.blackjack_model.loop_status = False

    def play_again(self):
        response = input("Would you like to play again (Y/N)? ").lower()
        if response == "y":
            return True
        if response == "n":
            return False
        if response not in ["y","n"]:
            self.play_again()
        