from Deck import Deck
from Player import Player

def calculate_score(player):
    score = 0
    for card in player.hand:
        if card.rank in ['J', 'Q', 'K']:
            score += 10
        elif card.rank == 'A':
            rank = None
            while rank not in [1, 11]:
                rank = int(input(f'{player.name}: You drew an Ace! Your current score is {player.score}. Would you like a 1, or an 11?'))
            score += rank
        else:
            score += int(card.rank)
            
    return score

def main():
    deck = Deck()
    
    print('Hello! Welcome to BlackJack. The game is get as close to 21 without going over.')
    print()
    print('Your objective is to beat the dealer. If you tie, its a \'push\'')
    print()
    
    players = []
    
    while True:
        name = input("What is your name? ")
        player = Player(name)
        players.append(player)
        
        add_another = ''
        while add_another not in ['y', 'n']:
            add_another = input('Would you like to add another player? y/n: ').lower()
            
        if add_another == 'n':
            break
        
    for player in players:
        print(player)
        
    dealer = Player('Dealer')
    
    deck.shuffle()
    deck.shuffle()
    deck.shuffle()
    
    for _ in range(2):
        for player in players:
            player.draw(deck)
        dealer.draw(deck)
        
    for player in players:
        player.score = calculate_score(player)
        print(player)
    
    dealer.score = calculate_score(dealer)
    print(dealer)
    
    

if __name__ == '__main__':
    main()