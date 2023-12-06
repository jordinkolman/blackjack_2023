import collections
import random

# Easy way to create cards without having to create a seperate class, since they have no methods
Card = collections.namedtuple("Card", ["rank", "suit"])


class Deck:
    # generator to create a rank list, and a list of suits
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        # combine each rank with each suit for a total of 52 combinations
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        # keeps actual list of cards abstract inside the deck
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    # Sightly better formatting for the printout of each card
    def __str__(self):
        sums = []
        for card in self._cards:
            rank = card.rank
            suit = card.suit
            card_sum = f"{rank} of {suit}"
            sums.append(card_sum)
        return str(sums)

    # Method uses random module to select a card at random and insert into a new, shuffled deck
    def shuffle(self):
        new_order = []
        while len(new_order) < 52:
            card = random.choice(self._cards)
            # makes sure the card has not already been added to the new shuffled deck
            if card in new_order:
                continue
            new_order.append(card)
        # sets card list to the new shuffled deck
        self._cards = new_order
        return self._cards

    # returns the top card and removes them from the deck
    def draw(self):
        card = self._cards[0]
        self._cards = self._cards[1:]
        return card


    # resets deck to a new 52 card ordered deck
    def reset(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]


# Some random statements to test correct implementation of the deck
if __name__ == "__main__":
    deck = Deck()
    print(deck)
    print()
    print()
    drawn = deck.draw(2)
    print(drawn)
    print(drawn in deck)
    deck = Deck()
    print(deck)
    print()
    deck.shuffle()
    print(deck)
    print()
    deck.reset()
    print(deck)
