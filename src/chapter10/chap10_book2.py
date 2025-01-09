"""
Exercise 1
Write a function that reads the words in words.txt and stores them as keys in a dictionary.
It doesn’t matter what the values are.
Then you can use the in operator as a fast way to check whether a string is in the dictionary.

If you did Exercise 10, you can compare the speed of this implementation with the list in operator
 and the bisection search.
 """


def read_words():
    """
    Reads a word list from a file named 'words.txt' and stores them in a dictionary.

    Returns:
        dict: A dictionary where keys are words from the file and values are None.
    """
    words = {}
    with open('words.txt') as file:
        for line in file:
            word = line.strip()
            words[word] = None
    return words


def search(dict_words: {}, item: str) -> bool:
    """
    Args:
        dict_words (dict): A dictionary of words.
        item (str): The word to search for in the dictionary.

    Returns:
        bool: True if the item is found in the dictionary, False otherwise.
    """
    return item in dict_words


assert search(read_words(), "apple") == True
assert search(read_words(), "kanker") == False

"""
Exercise 2
Read the documentation of the dictionary method setdefault and use it to write a more concise version of invert_dict.

"""


def invert_dict(dict_words: dict):
    inverse = {}
    for key in dict_words:
        val = dict_words[key]
        inverse.setdefault(val, []).append(key)
    return inverse


assert invert_dict(dict(a=1, b=2, c=3, z=1)) == {1: ['a', 'z'], 2: ['b'], 3: ['c']}

"""
Exercise 3   Memoize the Ackermann function from Exercise 2 and see if memoization makes it possible to evaluate
 the function with bigger arguments. Hint: no. Solution: https://thinkpython.com/code/ackermann_memo.py.
"""
#ToDo

"""
Exercise 4
If you did Exercise 7, you already have a function named has_duplicates that takes a list as a parameter and returns
True if there is any object that appears more than once in the list.

Use a dictionary to write a faster, simpler version of has_duplicates.
Solution: https://thinkpython.com/code/has_duplicates.py.

"""


def has_duplicates(words: list)->bool:
    dup = dict()
    for x in words:
        if x in dup:
            return True
        dup[x] = True
    return False

assert has_duplicates(["a", "b", "c", "a"]) == True


def has_duplicates_len(words: list)->bool:
   return len(set(list)) < len(list)

assert has_duplicates_len(["a", "b", "c", "a"]) == True

"""
Exercise 5
Two words are “rotate pairs” if you can rotate one of them and get the other (see rotate_word in Exercise 5).

Write a program that reads a wordlist and finds all the rotate pairs.
Solution: https://thinkpython.com/code/rotate_pairs.py.
"""


def rotate_pairs(words: list):
    pairs = {}
    for word in words:
        rotate_w = word[::-1]
        if rotate_w in words and word != rotate_w:
            pairs[word] = rotate_w
    return pairs


"""
Exercise 6
"""


def find_homophone_word(word_list, homophone_check):
    """
    Finds a five-letter word that meets the homophone conditions:
      - Removing the first letter produces a four-letter word that sounds the same.
      - Removing the second letter produces another four-letter word that sounds the same.

    Args:
    - word_list (set): A set of valid words.
    - homophone_check (function): A function to check if two words are homophones.

    Returns:
    - str: The five-letter word satisfying the conditions (if found), or None if no word matches.
    """
    for word in word_list:
        # Check for five-letter one-syllable words only
        if len(word) != 5:
            continue
        # Generate modified words
        without_first = word[1:]  # Remove the first letter
        without_second = word[0] + word[2:]  # Remove the second letter
        # Verify both are homophones of the original word
        if without_first in word_list and without_second in word_list:
            if homophone_check(word, without_first) and homophone_check(word, without_second):
                return word
    return None


# Dummy implementation for testing homophones
def dummy_homophone_check(word1, word2):
    # Replace this with a real homophone-checking function
    # For the purpose of this example, we assume that word1 and word2 are homophones if they are equal
    return word1.lower() == word2.lower()


# Example usage
if __name__ == "__main__":
    # Example word list
    word_list = {"wrack", "rack", "wack", "wright", "right", "rite", "write"}

    # Find the word
    result = find_homophone_word(word_list, dummy_homophone_check)
    print("The word is:", result)
