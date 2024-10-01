import random
import tkinter as tk
from tkinter import messagebox


def create_deck(card_of_interest, count_of_interest, total_deck_size):
    return [card_of_interest] * count_of_interest + ['other_card'] * (total_deck_size - count_of_interest)


def draw_cards(deck, num_draws):
    return random.sample(deck, num_draws)


def simulate_draws(card_of_interest, count_of_interest, total_deck_size, num_simulations, num_draws):
    deck = create_deck(card_of_interest, count_of_interest, total_deck_size)
    successes = 0
    total_cards_of_interest_drawn = 0

    for _ in range(num_simulations):
        drawn_cards = draw_cards(deck, num_draws)
        cards_of_interest_drawn = drawn_cards.count(card_of_interest)
        total_cards_of_interest_drawn += cards_of_interest_drawn
        if cards_of_interest_drawn > 0:
            successes += 1

    probability = successes / num_simulations
    average_drawn = total_cards_of_interest_drawn / num_simulations

    return probability, average_drawn


def run_simulation():
    card_of_interest = entry_card.get()
    count_of_interest = int(entry_count.get())
    total_deck_size = int(entry_total_deck.get())
    num_draws = int(entry_draws.get())
    num_simulations = int(entry_simulations.get())

    probability, average_drawn = simulate_draws(card_of_interest, count_of_interest, total_deck_size, num_simulations,
                                                num_draws)

    messagebox.showinfo("Simulation Results",
                        f"Probability of drawing at least one '{card_of_interest}': {probability:.2%}\n"
                        f"Average number of '{card_of_interest}' drawn: {average_drawn:.2f}")


# Set up the GUI window
window = tk.Tk()
window.title("MTG Draw Chance Simulator")

# Card of interest
tk.Label(window, text="Card of Interest:").grid(row=0, column=0)
entry_card = tk.Entry(window)
entry_card.grid(row=0, column=1)

# Number of cards of interest in the deck
tk.Label(window, text="Number of Card in Deck:").grid(row=1, column=0)
entry_count = tk.Entry(window)
entry_count.grid(row=1, column=1)

# Total deck size
tk.Label(window, text="Total Deck Size:").grid(row=2, column=0)
entry_total_deck = tk.Entry(window)
entry_total_deck.grid(row=2, column=1)

# Number of cards to draw
tk.Label(window, text="Number of Cards to Draw:").grid(row=3, column=0)
entry_draws = tk.Entry(window)
entry_draws.grid(row=3, column=1)

# Number of simulations
tk.Label(window, text="Number of Simulations:").grid(row=4, column=0)
entry_simulations = tk.Entry(window)
entry_simulations.grid(row=4, column=1)

# Run simulation button
run_button = tk.Button(window, text="Run Simulation", command=run_simulation)
run_button.grid(row=5, columnspan=2)

# Start the GUI event loop
window.mainloop()
