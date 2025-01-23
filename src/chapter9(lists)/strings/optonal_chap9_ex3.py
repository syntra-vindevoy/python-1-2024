from itertools import combinations
from collections import Counter


def count_valid_words(forbidden_letters, words):
    """
    Count the number of words that don't contain any forbidden letters.

    Parameters:
        forbidden_letters (str): A string of forbidden letters.
        words (list): A list of words to check.

    Returns:
        int: Number of valid words.
    """
    forbidden_set = set(forbidden_letters)
    valid_words = [word for word in words if not forbidden_set.intersection(word)]
    return len(valid_words)


def find_optimal_forbidden_letters(words):
    """
    Find the combination of 5 forbidden letters that excludes the smallest number of words.

    Parameters:
        words (list): A list of words to analyze.

    Returns:
        tuple: A tuple containing the optimal forbidden letters and the number of excluded words.
    """

    # Count occurrences of letters in all words
    letter_count = Counter(letter for word in words for letter in set(word))

    # Generate combinations of 5 most frequent letters
    letter_combinations = combinations(letter_count.keys(), 5)

    # Find the combination that excludes the smallest number of words
    min_excluded = float('inf')
    optimal_combination = None

    for combination in letter_combinations:
        excluded_count = len([word for word in words if any(letter in word for letter in combination)])
        if excluded_count < min_excluded:
            min_excluded = excluded_count
            optimal_combination = combination

    return optimal_combination, min_excluded


def main():

    with open("../words.txt") as file:
        words= [line.strip() for line in file]
    # Prompt user for forbidden letters and words
    forbidden_letters = "abxtv"

    # Define a sample word list or load your word list


    valid_word_count = count_valid_words(forbidden_letters, words)
    print(f"Number of valid words: {valid_word_count}")

    # Find optimal combination of 5 forbidden letters
    optimal_combination, excluded_count = find_optimal_forbidden_letters(words)
    print(f"Optimal forbidden letters: {''.join(optimal_combination)}")
    print(f"Excluded words with optimal letters: {excluded_count}")


if __name__ == "__main__":
    main()
