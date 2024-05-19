"""
Main program to set up and run a game of blackjack
"""

from player import Player
from blackjack_model import BlackJackModel
from blackjack_view import BlackJackTextView
from blackjack_controller import BlackJackTextController


def main():
    """
    main function to play blackjack
    """
    player1 = Player()
    blackjack_model = BlackJackModel()
    blackjack_view = BlackJackTextView(blackjack_model)
    blackjack_controller = BlackJackTextController(blackjack_model)
    blackjack_controller.wager()
    blackjack_model.deal_cards()
    blackjack_view.print_cards()
    if not blackjack_model.check_dealer_blackjack() and not blackjack_model.check_player_blackjack(blackjack_model.player_cards):
        while blackjack_model.loop_status is True:
            blackjack_controller.move()
            blackjack_view.print_cards()
            if blackjack_model.check_bust(blackjack_model.player_cards):
                break
        blackjack_model.dealer_moves()
    blackjack_view.output()
    if blackjack_controller.play_again():
        main()
main()
