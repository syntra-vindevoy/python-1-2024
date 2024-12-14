
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
from string import ascii_lowercase as ALPHABET
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

def has_all_chars_in_word(char_combination: str, word: str):
    return all(char in word for char in char_combination)


def has_any_char_in_word(char_combination: str, word: str):
    return any(char in word for char in char_combination)

def has_forbidden_char(forbidden_chars: str, word: str):
    return any(char in word for char in forbidden_chars)

def has_no_forbidden_char(forbidden_chars: str, word: str):
    return all(char not in word for char in forbidden_chars)

def get_char_combinations(characters:str):
    return {''.join(comb):0 for comb in combinations(characters, 5)}


def get_character_count(words: list):
    char_count = {char: 0 for char in ALPHABET}
    for char in ALPHABET:
        for word in words:
            if char in word:
                char_count[char] += 1
    return char_count

@time_execution
def main():
    words = get_wordlist_from_file("words.txt")
    character_count = get_character_count(words)
    character_count_sorted = sorted(character_count.items(), key=lambda x: x[1], reverse=True)
    sorted_alphabet= [char for char, count in character_count_sorted]
    char_combinations= get_char_combinations(sorted_alphabet) 

    #words = ["hello","kiekeboe"]
    for word in words:
        for combination in char_combinations:
            if has_forbidden_char(combination, word):
                char_combinations[combination] += 1
    
    pprint(char_combinations)

if __name__ == "__main__":
    main()

         
        





    
