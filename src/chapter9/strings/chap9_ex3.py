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

def find_best_forbidden_letters(word_list):
    """
    Write a program that prompts the user to enter a string of forbidden letters and then prints the number
    of words that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes the
    smallest number of words?
    Determines whether a given word contains any of the specified forbidden letters.
    If the word contains at least one forbidden letter, it returns False. Otherwise, it
    returns True.
    1. **Loading Words**: `load_words` reads all the words from a file into a list.
    2. **Avoids Function**: `avoids` checks if a word avoids a given set of forbidden letters.
    3. **Finding the Best Combination**:
    - `itertools.combinations` generates all combinations of 5 letters from the alphabet.
    - For each combination, the program counts the number of words excluded using the `avoids` function.
    - The program keeps track of the combination that results in the smallest number of excluded words.
    :param word_list:
    :return:
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    min_excluded = len(word_list)  # Start with the maximum possible value
    best_combination = None

    for combo in combinations(alphabet, 5):
        combo_str = ''.join(combo)
        excluded_count = sum(1 for word in word_list if not avoids(word, combo_str))
        if excluded_count < min_excluded:
            min_excluded = excluded_count
            best_combination = combo_str

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