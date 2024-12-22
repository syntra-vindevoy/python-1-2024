

from constants import *
from functions import *
from pprint import pprint


def eliminate_words(word_set, char_list):
    '''
    Eliminate words from word_set that contain any of the characters in char_list.
    '''
    new_word_set = set()
    for word in word_set:
        if not any(char in word for char in char_list):
            new_word_set.add(word)
    return new_word_set


def count_words_not_matching_chars(word_set, char_list):
    '''
    Count the number of words in word_set that do not contain any of the characters in char_list.
    '''
    return sum(1 for 
               word in word_set 
               if not any(char in word for char in char_list)
               )



@timing
def main():
    char_list = list(ALPHABET.value)
    word_set = set(get_wordlist_from_file("words.txt"))
    combination_set = get_5_char_combination_set(char_list)
    count_dict = {}

    for combination in combination_set:
        count_dict[combination]=count_words_not_matching_chars(word_set, combination)

if __name__ == "__main__":
    main()