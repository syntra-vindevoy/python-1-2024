
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
    combination_count_5_char_dictionary = {comb: 0 for comb in char_combinations}

    word_set = set(get_wordlist_from_file("words.txt"))
    char_list = ALPHABET.value
    char_dict = char_count(char_list,word_set)
    char_list_sorted = sorted(char_dict, key=char_dict.get, reverse=True)


    print(char_list_sorted)

    unmatched_words_x = word_set.copy()
    unmatched_combinations_x = char_combinations.copy()



    for i in range(20,22):
        print(char_i := char_list_sorted[i])
        matching_words_i = {word 
                            for word in unmatched_words_x 
                            if char_i in word}
        matching_combinations_i = {comb 
                                   for comb in unmatched_combinations_x 
                                   if char_i in comb}
        for combination in matching_combinations_i:
            combination_count_5_char_dictionary[combination] += len(matching_words_i)
        unmatched_words_i = unmatched_words_x - matching_words_i
        unmatched_combinations_i = unmatched_combinations_x - matching_combinations_i


        for j in range(i+1,23):
            char_j = char_list_sorted[j]
            matching_words_j = {word for word in unmatched_words_i if char_j in word}
            matching_combinations_j = {comb for comb in unmatched_combinations_i if char_j in comb}
            for combination in matching_combinations_j:
                combination_count_5_char_dictionary[combination] += len(matching_words_j)
            unmatched_words_j = unmatched_words_i - matching_words_j
            unmatched_combinations_j = unmatched_combinations_i - matching_combinations_j
            


            for k in range(j+1,24):
                char_k = char_list_sorted[k]
                matching_words_k = {word for word in unmatched_words_j if char_k in word}
                matching_combinations_k = {comb for comb in unmatched_combinations_j if char_k in comb}
                for combination in matching_combinations_k:
                    combination_count_5_char_dictionary[combination] += len(matching_words_k)
                unmatched_words_k = unmatched_words_j - matching_words_k
                unmatched_combinations_k = unmatched_combinations_j - matching_combinations_k
                


                for l in range(k+1,25):
                    char_l = char_list_sorted[l]
                    matching_words_l = {word for word in unmatched_words_k if char_l in word}
                    matching_combinations_l = {comb for comb in unmatched_combinations_k if char_l in comb}
                    for combination in matching_combinations_l:
                        combination_count_5_char_dictionary[combination] += len(matching_words_l)
                    unmatched_words_l = unmatched_words_k - matching_words_l
                    unmatched_combinations_l = unmatched_combinations_k - matching_combinations_l
                    


                    for m in range(l+1,26):
                        char_m = char_list_sorted[m]
                        matching_words_m = {word for word in unmatched_words_l if char_m in word}
                        matching_combinations_m = {comb for comb in unmatched_combinations_l if char_m in comb}
                        for combination in matching_combinations_m:
                            combination_count_5_char_dictionary[combination] += len(matching_words_m)
                        unmatched_words_m = unmatched_words_l - matching_words_m
                        unmatched_combinations_m = unmatched_combinations_l - matching_combinations_m
        '''
        '''
                        
    pprint(combination_count_5_char_dictionary)
    
    min_combination = min(combination_count_5_char_dictionary, key=combination_count_5_char_dictionary.get)
    print(f"The combination with the lowest value is: {min_combination} with {combination_count_5_char_dictionary[min_combination]} words")


    '''
    
 
    '''


        

        




















if __name__ == '__main__':
    main()






