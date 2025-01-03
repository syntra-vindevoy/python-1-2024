from itertools import combinations

def load_words(filename):
    """
    Loads words from a specified file, stripping whitespace from each line.

    This function reads a given text file line by line, processes each line to
    remove leading and trailing whitespace, and returns a list containing the
    processed lines. The function assumes that the input file is correctly
    formatted and accessible.

    :param filename: The path to the input file containing the list of words.
    :type filename: str
    :return: A list of words from the file with whitespace stripped.
    :rtype: list[str]
    """

    with open(filename) as file:
        return [line.strip() for line in file]


def ex3_avoid_letters_2(word: str, forbidden_letters: str):
    return word.index(forbidden_letters) == -1
from itertools import combinations

from itertools import combinations


def count_excluded_words(word_list, forbidden_letters):
    """
    Counts how many words in the given list are excluded by the provided forbidden letters.

    Args:
        word_list (list): List of words to check.
        forbidden_letters (set): A set of forbidden letters.

    Returns:
        int: The number of words that include any of the forbidden letters.
    """
    excluded_count = 0
    for word in word_list:
        # Check for any intersection between the word and the forbidden letters
        if forbidden_letters.intersection(word):  # Optimized membership check
            excluded_count += 1
    return excluded_count


def find_best_forbidden_letters(word_list):
    """
    Finds the combination of 5 forbidden letters that excludes the smallest number of words.

    Args:
        word_list (list): List of words to check.

    Returns:
        tuple: A tuple containing the best forbidden combination and the count of excluded words.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    min_excluded = len(word_list)  # Start with the maximum possible value
    best_combination = None

    # Iterate over all combinations of 5 letters
    for combo in combinations(alphabet, 5):
        forbidden_set = set(combo)  # Convert the combination to a set for faster lookups
        excluded_count = count_excluded_words(word_list, forbidden_set)

        if excluded_count < min_excluded:
            min_excluded = excluded_count
            best_combination = ''.join(combo)  # Convert back to a string for the result

    return best_combination, min_excluded




def avoids(word, forbidden_letters):
    """
      Exercise 3
    Write a function named avoids that takes a word and a string of forbidden letters, and that returns T
    rue if the word doesn’t use any of the forbidden letters.



    :param word: The word to be checked for forbidden letters.
    :type word: str
    :param forbidden_letters: A string containing letters that should not be present
        in the word.
    :type forbidden_letters: str
    :return: Returns True if the word does not contain any forbidden letters, otherwise
        returns False.
    :rtype: bool
    """
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True

assert avoids("alteridoticu", "aeiou") == False
assert avoids("alteridrrt", "aeiou") == False
assert avoids("skwlp", "aeiouy") == True


if __name__ == "__main__":
    best_comb, num_excluded = find_best_forbidden_letters(load_words("../words.txt"))
    print(f"The best combination of forbidden letters is: {best_comb}")
    print(f"It excludes {num_excluded} words.")