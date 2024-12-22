from itertools import combinations
from pprint import pprint
from constants import ALPHABET
from functions import get_wordlist_from_file

def main():
    char_list = list(ALPHABET.value)
    word_set = set(get_wordlist_from_file("words.txt"))

    combination_dict_1_chars = {}
    combination_dict_2_chars = {}
    combination_dict_3_chars = {}
    combination_dict_4_chars = {}
    combination_dict_5_chars = {}

    for comb in combinations(char_list, 1):
        char_comb = comb
        set_comb = {word for word in word_set if all(char in word for char in char_comb)}
        combination_dict_1_chars[char_comb] = set_comb

    for comb in combinations(char_list, 2):
        char_comb = ''.join(comb)
        set_comb = {word for word in word_set if all(char in word for char in char_comb)}
        combination_dict_2_chars[char_comb] = set_comb

    for comb in combinations(char_list, 3):
        char_comb = ''.join(comb)
        set_comb = {word for word in word_set if all(char in word for char in char_comb)}
        combination_dict_3_chars[char_comb] = set_comb

    for comb in combinations(char_list, 4):
        char_comb = ''.join(comb)
        set_comb = {word for word in word_set if all(char in word for char in char_comb)}
        combination_dict_4_chars[char_comb] = set_comb

    for comb in combinations(char_list, 5):
        char_comb = ''.join(comb)
        set_comb = {word for word in word_set if all(char in word for char in char_comb)}
        combination_dict_5_chars[char_comb] = set_comb

    pprint(combination_dict_5_chars['abcde'])

if __name__ == "__main__":
    main()