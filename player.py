"""
Player class used for the 
"""

class Player:
    """
    player class
    """

    def __init__(self):
        self._money = 500
        self._wager = 0
        self._table_position = None
        self._cards = []

    def set_wager(self, amount):
        self._money -= amount
    
    @property
    def money(self):
        return self._money