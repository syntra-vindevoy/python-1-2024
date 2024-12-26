
from itertools import combinations
from os import path
from pprint import pprint
from time import time
from constants import *
from icecream import ic

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Time taken to execute {func.__name__}:{end_time - start_time:.4f} seconds")
        return result
    return wrapper

def loop_function(function,amount,depth):
    for i in range(amount):
        function()

def get_5_char_combination_set(character_stringlist):
    character_combinations = set()
    length = len(character_stringlist)
    

    for i in range(0,length-4):
        char_1 = character_stringlist[i]
        for j in range (i+1,length-3):
            char_2 = character_stringlist[j]
            for k in range (j+1,length-2):
                char_3 = character_stringlist[k]
                for l in range (k+1,length-1):
                    char_4 = character_stringlist[l]
                    for m in range (l+1,length):
                        char_5 = character_stringlist[m]
                        character_combinations \
                        .add(''.join([char_1,char_2,char_3,char_4,char_5]))
    return character_combinations   

def get_all_char_combination_set(character_stringlist):
    character_combinations = set()
    length = len(character_stringlist)

    for i in range(0,length-4):
        char_1 = character_stringlist[i]
        character_combinations.add(''.join([char_1]))
        for j in range (i+1,length-3):
            char_2 = character_stringlist[j]
            character_combinations.add(''.join([char_1,char_2]))
            for k in range (j+1,length-2):
                char_3 = character_stringlist[k]
                character_combinations.add(''.join([char_1,char_2,char_3]))
                for l in range (k+1,length-1):
                    char_4 = character_stringlist[l]
                    character_combinations.add(''.join([char_1,char_2,char_3,char_4]))
                    for m in range (l+1,length):
                        char_5 = character_stringlist[m]
                        character_combinations \
                        .add(''.join([char_1,char_2,char_3,char_4,char_5]))
    return character_combinations  

def get_char_combination_set(character_stringlist, combination_length):
    character_combinations = set()
    for combo in combinations(character_stringlist, combination_length):
        character_combinations.add(''.join(combo))
    return character_combinations

def get_char_combination_list(character_stringlist, combination_length):
    character_combinations = list()
    for combo in combinations(character_stringlist, combination_length):
        character_combinations.append(''.join(combo))
    return character_combinations

def get_wordlist_from_file(file_name: str):
    script_dir = path.dirname(__file__)

    file_path = path.join(script_dir, file_name)
    with open(file_path, "r") as f:
        words = f.read().split("\n")
    return words

def char_count(char_list,word_set):
    char_dict = {char: 0 for char in char_list}
    for word in word_set:
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
    return char_dict

def char_in_word(char,word):
    return char in word

def char_not_in_word(char,word):
    return not char in word

def char_in_words(char:str,word_set:set[str])->set[str]:
    return {word for word in word_set if char in word}

def char_not_in_words(char:str,word_set:set[str])->set[str]:
    return {word for word in word_set if not char in word}

def any_char_in_word(char_list:set[str],word:str)->bool:
    return any([char in word for char in char_list])

def no_char_in_word(char_list, word):
    return all(char not in word for char in char_list)

def any_char_in_words(char_list:set[str],word_set:set[str])->set[str]:
    return {word for word in word_set if any_char_in_word(char_list,word)}

def no_char_in_words(char_list:set[str],word_set:set[str])->set[str]:
    return {word for word in word_set if no_char_in_word(char_list,word)}

def word_to_set(word:str)->set[str]:
    return set(word)


def get_matching_dict_slow(chars,char_combination_length,word_set):
    char_combinations = get_char_combination_set(chars,char_combination_length) 
    adding_dict = {comb: 0 for comb in char_combinations}
    for comb in char_combinations:
        adding_dict[comb] += len(any_char_in_words(comb,word_set))
    return adding_dict

def get_matching_dict_adding(chars, char_combination_length, word_set):
    char_combination_set = \
        get_char_combination_set(chars, char_combination_length)
    combination_dict = \
        {comb: 0 for comb in char_combination_set}
    word_dict = \
        {word: char_combination_set.copy() for word in word_set}
    for char in chars:
        word_matched_list = \
            [word for word in word_set if char in word]
        combination_matched_list = \
            [comb for comb in char_combination_set if char in comb]
        for word in word_matched_list:
            word_dict[word] -= set(combination_matched_list)
    for comb in combination_dict:
        combination_dict[comb] = sum(1 for word in word_dict if comb not in word_dict[word])
    return combination_dict

from collections import defaultdict
import itertools

def get_matching_dict_adding_beta(chars, length, word_set):
    matching_dict = defaultdict(list)
    combinations = {''.join(comb) for comb in itertools.product(chars, repeat=length)}
    
    for word in word_set:
        for comb_str in combinations:
            if comb_str in word:
                matching_dict[comb_str].append(word)
    
    return matching_dict

from collections import defaultdict
import itertools

def get_matching_count(chars, length, word_set):
    match_count = defaultdict(int)
    combinations = get_char_combination_set(chars, length)
    ic(combinations)
    


    return match_count