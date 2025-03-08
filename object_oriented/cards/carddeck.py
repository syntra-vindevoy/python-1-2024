
class Carddeck:
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    def __init__(self):
        super().__init__()
        self.deck = []
        for suit in self.suits:
            for number in self.numbers:
                self.deck.append((suit, number))
