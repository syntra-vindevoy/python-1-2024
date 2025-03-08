
from card_methods import New_deck, DrawCard

deck1 = New_deck
deck1.shuffle()
deck1.show_deck_list()

pulled_cards = []
for i in range (100):
    draw_one = DrawCard()
    card, deck1.deck = draw_one.draw_card(deck1.deck)
    pulled_cards.append(card)

    print(f"Pulled cards: {pulled_cards}")
    print(f"Remaining cards: {len(deck1.deck)} {deck1.deck}")
