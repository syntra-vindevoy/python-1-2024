
from itertools import combinations
from pprint import pprint
import os
import time

import string
ALPHABET = string.ascii_lowercase

def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper



def get_char_combinations():
    return {''.join(comb):0 for comb in combinations(ALPHABET, 5)}


def get_wordlist_from_file(file: str):
    script_dir = os.path.dirname(__file__)
    file_name = "words.txt"
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, "r") as f:
        words = f.read().split("\n")
    return words


def has_all_chars_in_word(char_combination: str, word: str):
    return all(char in word for char in char_combination)


@time_execution
def main():
    char_combinations = get_char_combinations()
    words = get_wordlist_from_file("words.txt")
    # pprint(char_combinations)
    # pprint(words)
    for word in words:
        for combination in char_combinations:
            if has_all_chars_in_word(combination, word):
                char_combinations[combination] += 1
    pprint(char_combinations)

'''

'''



if __name__ == "__main__":
    main()

