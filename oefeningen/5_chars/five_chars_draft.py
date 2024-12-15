
'''
Exercise 9.3. 

Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.

Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don’t contain any of them. 

Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
'''


from itertools import combinations
import os
from string import ascii_lowercase as alphabet
from pprint import pprint
import time

def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken to execute {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper


def get_wordlist_from_file(file: str):
    script_dir = os.path.dirname(__file__)
    file_name = "words.txt"
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, "r") as f:
        words = f.read().split("\n")
    return words


def get_filestring(file: str):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file)
    with open(file_path, "r") as f:
        filestring = f.read()
    return filestring


def has_forbidden_char(forbidden_chars: str, word: str):
    return any(char in word for char in forbidden_chars)

def get_char_combinations(characters:str):
    char_combinations= {}
    for comb in combinations(characters, i):
        char_combinations[comb] = 0


def get_character_count(words: list):
    char_count = {char: 0 for char in alphabet}
    for char in alphabet:
        for word in words:
            if char in word:
                char_count[char] += 1
    return char_count

def remove_items_containing_char_from_list(char: str, list: list):
    return [word for word in list if char not in word]

def add_one_to_dict_values_for_keys_containing_char(char: str, dict: dict):
    for key in dict.keys():
        if char in key:
            dict[key] += 1
    return dict

@time_execution
def get_combinations(character_stringlist):
    character_combinations = []
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
                        character_combinations.append(''.join([char_1,char_2,char_3,char_4,char_5]))
    return character_combinations

def get_dict_from_list(combinations_list):
    combinations_dict = {}
    for combination in combinations_list:
        combination_str = ''.join(combination)
        combinations_dict[combination_str] = 0
    return combinations_dict

def get_matching_items(char,combination_list):
    return [combination for combination in combination_list if char in combination]

@time_execution
def main():
    word_list = get_wordlist_from_file("words.txt")

    character_count = get_character_count(word_list)
    character_count_sorted = sorted(character_count.items(), key=lambda x: x[1], reverse=True)
    sorted_alphabet= [char for char, count in character_count_sorted]
    combination_list = get_combinations(sorted_alphabet)
    combination_dict = get_dict_from_list(combination_list)


    '''
    # test variables
    '''
    char_list = ['a','e','d']
    combination_list = ["ae","ad","de"]
    combination_dict = {'ae':0,'ad':0,'de':0}
    word_list = ['apple','zzyx']

    for char in char_list: # a tot z
        #pprint(matching_combinations)
        matching_words = get_matching_items(char,word_list)
        matching_combinations = get_matching_items(char,combination_list)
        pprint(matching_words)
        print()

               
        


                        
                        
                         
            




    





if __name__ == "__main__":
    main()







    
