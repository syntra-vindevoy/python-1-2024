
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
    char_combinations = get_5_char_combination_set(ALPHABET.value)
    combination_dictionary = {comb: 0 for comb in char_combinations}
    #pprint(combination_dictionary)

    word_set = set(get_wordlist_from_file("words.txt"))
    char_list = ALPHABET.value
    char_dict = char_count(char_list,word_set)
    char_list_sorted = sorted(char_dict, key=char_dict.get, reverse=True)

    #print(char_list)



    for i in range(0,26):
        char = char_list[i]
        matching_words_i = \
            {word for word in word_set.copy() if char in word}
        matching_combinations_i = \
            {comb for comb in char_combinations.copy() if char in comb} 
        for combination in matching_combinations_i:
            combination_dictionary[combination] += len(matching_words_i)

    pprint(combination_dictionary)
    
    min_combination = min(combination_dictionary, key=combination_dictionary.get)
    print(f"The combination with the lowest value is: {min_combination} with {combination_dictionary[min_combination]} words")

if __name__ == '__main__':
    main()






