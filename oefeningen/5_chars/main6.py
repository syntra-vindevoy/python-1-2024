
'''
Exercise 9.3. 

Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.

Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don’t contain any of them. 

Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
'''

from time import time
from functions import *
from constants import *

from icecream import ic

@timing
def main():

    # creating a dictionary with all possible 5 character combinations to keep track of numbers
    #pprint(combination_dictionary)

    word_set = set(get_wordlist_from_file("words.txt"))
    length = len(word_set)
    char_list = ALPHABET.value
    char_dict = char_count(char_list,word_set)
    char_list_sorted = sorted(char_dict, key=char_dict.get, reverse=True)

    char_combinations = get_5_char_combination_set(char_list_sorted)
    combination_dictionary = {comb: length for comb in char_combinations}

    words_x = word_set.copy()

    for i in range(0,26):
        char = char_list_sorted[i]
        char_not_in_words_i = \
            {word for word in words_x if char not in word}
        for j in range(1, 26):
            char_not_in_words


    pprint(combination_dictionary)
    
    min_combination = min(combination_dictionary, key=combination_dictionary.get)
    print(f"The combination with the lowest value is: {min_combination} with {combination_dictionary[min_combination]} words")

    max_combination = max(combination_dictionary, key=combination_dictionary.get)
    print(f"The combination with the highest value is: {max_combination} with {combination_dictionary[max_combination]} words")


if __name__ == '__main__':
    main()






