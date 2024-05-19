"""
Unit tests for blackjack_model.py file
"""

from player import Player
from blackjack_model import BlackJackModel

player1 = Player()
test = BlackJackModel([player1])

def test_calculate_hand_value():
    """
    doctring
    """
    assert test.calculate_hand_value([Card("Spade", 1), Card("Spade", 10)]) == 21
    assert test.calculate_hand_value([Card("Spade", 1), Card("Spade", 1)]) == 12
    assert test.calculate_hand_value([Card("Spade", 12), Card("Spade", 13)]) == 20