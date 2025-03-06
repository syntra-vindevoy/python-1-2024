import random

class Carddeck ():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    def __init__(self):
        super().__init__()
        self.deck = []
        for suit in self.suits:
            for number in self.numbers:
                self.deck.append((suit, number))


class Shuffle(Carddeck):
    def __init__(self):
        super().__init__()

    def shuffle(self):
        random.shuffle(self.deck)


class Printdeck (Shuffle):
    def __init__(self):
        super().__init__()

    def show_deck(self):
        for card in self.deck:
            print(f"{card[1]} of {card[0]}")

    def show_deck_list(self):
        print (self.deck)

#only to create deck
carddeck = Carddeck()
print (carddeck.deck)

#create and shuffle
shuffled_deck = Shuffle()
shuffled_deck.shuffle()
print (shuffled_deck.deck)

#create, shuffle and print function
new_deck = Printdeck()
new_deck.show_deck()
new_deck.show_deck_list()
new_deck.shuffle()
new_deck.show_deck_list()
