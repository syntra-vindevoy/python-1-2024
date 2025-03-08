from shuffle import Shuffle

class Printdeck (Shuffle):
    def __init__(self):
        super().__init__()

    def show_deck(self):
        for card in self.deck:
            print(f"{card[1]} of {card[0]}")

    def show_deck_list(self):
        print (self.deck)
