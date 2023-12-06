from Deck import Deck
from random import choice

def card_string(card):
    return f'{card.rank}{card.suit}'

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        
    def __str__(self):
        return f'Player: {self.name}  Face Up: {[card_string(card) for card in self.hand[1:]]}'
    
    @property
    def hand(self):
        return self._hand
    
    @hand.setter
    def hand(self, hand):
        self._hand = hand
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score
        
    def calc_score(self, card):
        if card.rank in ['J', 'Q', 'K']:
            rank = 10
        elif card.rank == 'A':
            rank = None
            while rank not in [1, 11]:
                if self.name == 'Dealer':
                    if self.score <= 10:
                        rank = 11
                    else:
                        rank = 1
                else:
                    rank = int(input(f'Your current score is {self.score}. Would you like a 1, or an 11 for this Ace?: '))
        else:
            rank = int(card.rank)
            
        return rank
                
    def draw(self, deck):
        card = deck.draw()
        self.score += self.calc_score(card)
        self.hand.append(card)
        
        return self.hand
    
    def reset_hand(self):
        self.hand = []
        
    def show_hand(self):
        return [card_string(card) for card in self.hand]
    

if __name__ == '__main__':
    player1 = Player('Jordin')
    print(f'Name: {player1.name}')
    player1.name = 'J'
    print(f'Name: {player1.name}')
    print(f'Hand: {player1.hand}')
    deck1 = Deck()
    player1.draw(deck1)
    print(deck1)
    print(f'Hand: {player1.hand}')
    print(player1.score)
    player1.score = 10
    print(player1.score)