from Deck import Deck
from Player import Player
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_ui(players, dealer, current_player=None):
    clear()
    print('Blackjack ♠ ♥ ♣ ♦\n\n')
    
    for player in players:
        print(player, end='\n\n')
    print(dealer, end='\n\n')
    
    if current_player:
        print(f'Current Player: {current_player.name}\n')
        print(f'Your Hand: {current_player.show_hand()}  Your Score: {current_player.score}\n\n')

    

def game(players, dealer, deck):
    deck.shuffle()
    deck.shuffle()
    deck.shuffle()

    print_ui(players, dealer, players[0])

    for _ in range(2):
        for player in players:
            player.draw(deck)
        dealer.draw(deck)
    
    for player in players:
        print_ui(players, dealer, player)
        
        hit_choice = input('Would you like to hit, or stay?: ')
        while player.score < 21 and hit_choice != 'stay':
            while hit_choice != 'stay':
                player.draw(deck)
                print_ui(players, dealer, player)
                if player.score >= 21:
                    break
                hit_choice = input('Would you like to hit, or stay?: ')

        if player.score > 21:
            print('You busted! Game Over. Next Player! ')
            cont = input('press enter to continue')
            continue
        
        clear()
        print('Blackjack ♠ ♥ ♣ ♦\n\n')
        print(f'Current Player: {player.name}')
        print(f'Final Score: {player.score}')
        print(f'Hand: {player.show_hand()}')
        cont = input('press enter to continue')
    
    while dealer.score <= 16:
        dealer.draw(deck)

    winners = []

    for player in players:
        if dealer.score > 21:
            if player.score <= 21:
                winners.append(player)
        else:
            if 21 >= player.score > dealer.score:
                winners.append(player)
            elif 21 >= player.score == dealer.score:
                print(f'{player.name}: You tied with the dealer. Result is a push.')
            
            if len(winners) == 0:
                winners.append(dealer)
            
    return winners


def main():
    deck = Deck()
    play_again = None

    clear()
    print('Blackjack ♠ ♥ ♣ ♦ \n\n')
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
        

    dealer = Player('Dealer')

    while play_again != 'n':
        clear()
        deck.reset()
        for player in players:
            player.reset_hand()
            player.score = 0
        dealer.reset_hand()
        dealer.score = 0
        
        print_ui(players, dealer)

        winners = game(players, dealer, deck)
        
        clear()
        print('Blackjack ♠ ♥ ♣ ♦\n\n')

        if dealer in winners:
            print('Sorry. The dealer won this round!\n')
        else:
            print(f'Congratulations! The following players beat the dealer: {[winner.name for winner in winners]}\n')
            
        
        print(f'Final Scores: ')
        for player in players:
            print(f'{player.name}: {player.score} Hand: {player.show_hand()}')
        print(f'Dealer: {dealer.score} Hand: {dealer.show_hand()}\n')

        while True:
            play_again = input('Play Again? y/n: ').lower()
            if play_again in ['y', 'n']:
                break



if __name__ == '__main__':
    main()