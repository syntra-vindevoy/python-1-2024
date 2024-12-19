
'''
Exercise 9.3. 

Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.

Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don’t contain any of them. 

Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
'''

# trying to migrate to a set instead of a list, due to faster retrieval


from itertools import combinations
from string import ascii_lowercase as alphabet
from pprint import pprint
from collections import Counter

import time
import os


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken to execute {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper


@timing
def get_wordlist_from_file(file: str):
    script_dir = os.path.dirname(__file__)
    file_name = "words.txt"
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, "r") as f:
        words = f.read().split("\n")
    return words


@timing
def get_character_count(words: list):
    char_count = {char: 0 for char in alphabet}
    for char in alphabet:
        for word in words:
            if char in word:
                char_count[char] += 1
    return char_count


#
# @timing
# def get_character_count_2(words: list):
#   char_count = Counter()
#    for word in words:
#        unique_chars = set(word)  # To avoid counting the same character multiple times in a word
#        char_count.update(unique_chars)
#    return {char: char_count[char] for char in alphabet}
#

@timing
def get_combination_set(character_stringlist):
    character_combinations = set()
    for i in range(0,26):
        char_1 = alphabet[i]
        for j in range (i+1,26):
            char_2 = alphabet[j]
            for k in range (j+1,26):
                char_3 = alphabet[k]
                for l in range (k+1,26):
                    char_4 = alphabet[l]
                    for m in range (l+1,26):
                        char_5 = alphabet[m]
                        character_combinations.add(''.join([char_1,char_2,char_3,char_4,char_5]))
    return character_combinations    


@timing
def get_dict_from_set(combination_set):
    combinations_dict = {}
    for combination in combination_set:
        combination_str = ''.join(combination)
        combinations_dict[combination_str] = 0
    return combinations_dict


def get_matching_items_from_set(char, word_set):
    return [word for word in word_set if char in word]


@timing
def main():
    word_list = get_wordlist_from_file("words.txt")
    character_count = get_character_count(word_list)
    character_count_sorted = sorted(character_count.items(), key=lambda x: x[1], reverse=True)
    sorted_alphabet = [char for char, count in character_count_sorted]
    
    char_list = sorted_alphabet
    combination_original_set = get_combination_set(sorted_alphabet)
    combination_dict = get_dict_from_set(combination_original_set)

    for char in char_list: 
        combination_set = combination_original_set.copy()
        matching_words = get_matching_items_from_set(char, word_list) 
        matching_combinations = get_matching_items_from_set(char, combination_set)

        for matching_combination in matching_combinations:
            combination_dict[matching_combination] += len(matching_words)
            combination_set.remove(matching_combination)
        
    min_value = min(combination_dict.values())
    smallest_combinations = [k for k, v in combination_dict.items() if v == min_value]
    print("Combinations with the smallest value:")
    pprint(smallest_combinations)   

    # max_value = max(combination_dict.values())
    # largest_combinations = [k for k, v in combination_dict.items() if v == max_value]
    # print("Combinations with the largest value:")
    # pprint(largest_combinations)  

if __name__ == "__main__":
    main()

               








    
