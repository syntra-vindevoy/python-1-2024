import random


class Carddeck:
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    def __init__(self):
        super().__init__()
        self.deck = []
        self.start()

    def start(self):
        self.deck = []
        for suit in self.suits:
            for number in self.numbers:
                self.deck.append((suit, number))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def show(self):
        print (self.deck)

    def draw(self):
        if len(self.deck) == 0:
            print ("No more cards to draw")
            return None
        else:
            card = self.deck[0]
            self.deck = self.deck[1:]
            return card
    @property
    def remaining(self):
        return len(self.deck)

c = Carddeck()
c.show()
for i in range(3):

    d = c.draw()
    print (d)
print(c.remaining)



