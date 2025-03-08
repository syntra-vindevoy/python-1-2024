
class DrawCard:
    def __init__(self):
        self.card = None

    def draw_card(self, cards):
        if len(cards) == 0:
            print ("No more cards to draw")
            return None, cards
        else:
            self.card = cards[0]
            remaining_cards = cards[1:]
            return self.card, remaining_cards
