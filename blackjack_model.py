"""
Playing a game of BlackJack
"""
from deck_of_cards import Deck

class BlackJackModel:
    """
    BlackJack Game
    """

    def __init__(self):
        self._deck = Deck()
        self._wager = 0
        self._player_cards = []
        self._dealer_cards = []
        self._money = 500
        self.loop_status = True
        self._deck.shuffle_deck()
    
    def set_wager(self, amount):
        self._wager = amount

    def deal_cards(self):
        for _ in range(2):
            self._player_cards.append(self._deck.select_top_card())
            self._dealer_cards.append(self._deck.select_top_card())

    def value(self, cards):
        hand_value = 0
        for card in cards:
            if card.number in ["J", "Q", "K"]:
                hand_value += 10
            elif card.number == "A":
                if hand_value <= 10:
                    hand_value +=11
                else:
                    hand_value +=1
            else:
                hand_value += card.number
        return hand_value
    
    def check_if_can_hit(self, cards):
        if self.value(cards) < 21:
            return True
        return False
    
    def check_if_can_split(self, cards):
        if len(self._player_cards) == 2 and cards[0].number == cards[1].number:
            return True
        return False
    
    def check_if_can_double_down(self, cards):
        if len(cards) == 2:
            if self.value(cards) in [16, 17, 18] and (cards[0].number == "A" or cards[1].number == "A"):
                return True
            if self.value(cards) in [9, 10, 11] and (cards[0].number != "A" and cards[1].number != "A"):
                return True
            if self.value(cards) <= 11:
                return True
        return False
    
    def hit(self, hand):
        hit_card = self._deck.select_top_card()
        hand.append(hit_card)
        return hit_card
    
    def split(self):
        pass

    def double_down(self):
        pass

    def check_dealer_blackjack(self):
        if self.value(self._dealer_cards) == 21 and len(self._dealer_cards) == 2:
            return True
        return False
    
    def check_player_blackjack(self, cards):
        if self.value(cards) == 21 and len(cards) == 2:
            return True
        return False
    
    def check_bust(self, cards):
        if self.value(cards) > 21:
            return True
        return False
    
    def dealer_moves(self):
        while self.value(self._dealer_cards) <= 16:
            self.hit(self._dealer_cards)
        return self.value(self._dealer_cards)
    
    @property
    def money(self):
        return self._money
    
    @property
    def player_cards(self):
        return self._player_cards
    
    @property
    def dealer_cards(self):
        return self._dealer_cards
    
    @property
    def wager(self):
        return self._wager

