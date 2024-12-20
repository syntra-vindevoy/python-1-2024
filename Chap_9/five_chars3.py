import string
from collections import Counter
from datetime import datetime
from itertools import combinations


def word_to_bitmask(word):
    """Convert a word into a bitmask based on its characters."""
    mask = 0
    for letter in word:
        mask |= 1 << (ord(letter) - ord('a'))
    return mask


def count_letter_frequencies(words):
    """Count frequency of each letter in the list of words."""
    letter_counts = Counter(letter for word in words for letter in set(word))
    # Create a list sorted alphabetically by letter, then by frequency in ascending order
    sorted_letters = sorted(string.ascii_lowercase, key=lambda l: (letter_counts[l], l))
    return sorted_letters, letter_counts


def evaluate_combo(fixed_three, additional_two, word_bitmasks):
    """Evaluate how many words a combination of 5 letters can form."""
    # Convert additional_two to a list to enable concatenation
    combo_mask = sum(1 << (ord(c) - ord('a')) for c in fixed_three + list(additional_two))
    # Count the number of words that are formable
    count_words = sum(1 for word_mask in word_bitmasks if word_mask & combo_mask == 0)
    return count_words


def find_best_combo_with_two(words):
    """Find the best 5-letter combination: 3 fixed + 2 dynamic."""
    # Precompute bitmasks for all words
    word_bitmasks = [word_to_bitmask(word) for word in words]

    # Count letter frequencies and find the least used letters
    sorted_letters, letter_counts = count_letter_frequencies(words)

    # Select the 3 least-used letters
    fixed_three = sorted_letters[:3]
    print(f"The 3 least-used letters are: {fixed_three}")

    # Generate all possible combinations of 2 additional letters
    remaining_letters = [l for l in string.ascii_lowercase if l not in fixed_three]
    all_combinations = combinations(remaining_letters, 2)

    best_combo = None
    max_words_left = 0

    for additional_two in all_combinations:
        words_left = evaluate_combo(fixed_three, additional_two, word_bitmasks)
        if words_left > max_words_left:
            max_words_left = words_left
            best_combo = fixed_three + list(additional_two)

    # Return the best combination and associated information
    return ''.join(best_combo), max_words_left


if __name__ == "__main__":
    start = datetime.now()
    # Read the list of words
    with open("words.txt", "r") as file:
        words = file.read().splitlines()

    best_combo, max_words = find_best_combo_with_two(words)
    end = datetime.now()
    print("Time taken:", end - start)
    # Print results
    print("Best combination:", best_combo)
    print("Maximum words formable:", max_words)
