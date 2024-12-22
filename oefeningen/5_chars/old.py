


'''
Exercise 9.3. 

Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.

Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don’t contain any of them. 

Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
'''


from itertools import product
from string import ascii_lowercase as alphabet

from time import time
from os import path
from pprint import pprint 
from icecream import ic

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Time taken to execute {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper


def get_wordlist_from_file(file: str):
    script_dir = path.dirname(__file__)
    file_name = "words.txt"
    file_path = path.join(script_dir, file_name)
    with open(file_path, "r") as f:
        words = f.read().split("\n")
    return words


def get_character_count(words: list):
    char_count = {char: 0 for char in alphabet}
    for char in alphabet:
        for word in words:
            if char in word:
                char_count[char] += 1
    return char_count


def get_5_char_combination_set(character_stringlist):
    character_combinations = set()
    length = len(character_stringlist)
    for i in range(0,length):
        char_1 = character_stringlist[i]
        for j in range (i+1,length):
            char_2 = character_stringlist[j]
            for k in range (j+1,length):
                char_3 = character_stringlist[k]
                for l in range (k+1,length):
                    char_4 = character_stringlist[l]
                    for m in range (l+1,length):
                        char_5 = character_stringlist[m]
                        character_combinations.add(''.join([char_1,char_2,char_3,char_4,char_5]))
    return character_combinations    

def get_4_char_combination_set(character_stringlist):
    character_combinations = set()
    length = len(character_stringlist)
    for i in range(0,length):
        char_1 = character_stringlist[i]
        for j in range (i+1,length):
            char_2 = character_stringlist[j]
            for k in range (j+1,length):
                char_3 = character_stringlist[k]
                for l in range (k+1,length):
                    char_4 = character_stringlist[l]
                    character_combinations.add(''.join([char_1,char_2,char_3,char_4]))
    return character_combinations  

def get_3_char_combination_set(character_stringlist):
    character_combinations = set()
    length = len(character_stringlist)
    for i in range(0,length):
        char_1 = character_stringlist[i]
        for j in range (i+1,length):
            char_2 = character_stringlist[j]
            for k in range (j+1,length):
                char_3 = character_stringlist[k]
                character_combinations.add(''.join([char_1,char_2,char_3]))
    return character_combinations

def get_2_char_combination_set(character_stringlist):
    character_combinations = set()
    length = len(character_stringlist)
    for i in range(0,length):
        char_1 = character_stringlist[i]
        for j in range (i+1,length):
            char_2 = character_stringlist[j]
            character_combinations.add(''.join([char_1,char_2]))
    return character_combinations

def get_dict_from_set(combination_set):
    return {combination: 0 for combination in combination_set}

def get_matching_items_from_set(char, word_set):
    return [word for word in word_set if char in word]

def combine_two_iterables(iter_1, iter_2):
    return set(product(iter_1, iter_2))


@timing
def main():
    ic.disable()
    word_list = get_wordlist_from_file("words.txt")
    '''
    word_list = [
        #'apple',
        'banana',
        #'orange',
        #'kiwi',
        #'mango',
        #'zucchini',
        ]
    '''
    #word_list = word_list[:100]
    ic(word_list)
    character_count = get_character_count(word_list)
    character_count_sorted = sorted(
        character_count.items(), 
        key=lambda x: x[1], 
        reverse=True
        )
    sorted_alphabet = [char for char, count in character_count_sorted]

    char_list = sorted_alphabet
    '''
    char_list = (
                'a',
                'z',
                'o',
                'u',
                'i',
                'e'
                 )
    '''
    ic(char_list)

    combination_original_set = get_5_char_combination_set(char_list)
    ic(combination_original_set)

    combination_dict = get_dict_from_set(combination_original_set)
    ic(combination_dict)
    # reward matching items

    for char_index in range(0, len(char_list)): # a tot z
        ic(char_list[char_index])
        combination_set = combination_original_set.copy()
        matching_words = get_matching_items_from_set(
            char_list[char_index], 
            word_list) 
        matching_combinations = get_matching_items_from_set(
            char_list[char_index], 
            combination_set)
 
        ic(matching_combinations)
        ic(matching_words)

        # reward matching items
        for matching_combination in matching_combinations:
            combination_dict[matching_combination] += len(matching_words)
    
        # punish double matching items
        punishment_set = set()
        for char_sub_index in range(char_index + 1, len(char_list)):
            sub_matching_combinations = \
                get_matching_items_from_set(
                    char_list[char_sub_index], 
                    matching_combinations)
            sub_matching_words = \
                get_matching_items_from_set(
                    char_list[char_sub_index], 
                    matching_words)
            punishment_set.update(
                set(
                    product(
                        sub_matching_combinations, 
                        sub_matching_words
                        )))
            

    ic(combination_dict)

    min_value = min(combination_dict.values())
    smallest_combinations = [
                            k for k, v in combination_dict.items() 
                            if v == min_value 
                            ]
    ic(smallest_combinations)
    pprint(combination_dict)
    print("Combinations with the smallest value:")
    print(f"Minimum value: {min_value}")
    print(smallest_combinations) 
    ic.enable()

    ''' test
    '''
    
if __name__ == "__main__":
    main()