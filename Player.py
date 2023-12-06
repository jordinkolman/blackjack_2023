from Deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        
    def __str__(self):
        def card_string(card):
            return f'{card.rank} of {card.suit}'
        return f'Player: {self.name}  Score: {self.score}  Hand: {[card_string(card) for card in self.hand]}'
    
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
        
    def draw(self, deck):
        self.hand.append(deck.draw())
        return self.hand
    

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