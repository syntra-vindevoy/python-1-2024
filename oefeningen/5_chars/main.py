
from functions import *
from collections import defaultdict


### FINISHED CODE ###
@timing
def main_matched(char_frozen_set,word_frozen_set):

    comb_matched_dict = dict()
    for char in char_frozen_set:
        comb_matched_dict[char]=set()
    
# 1 char
    for char in char_frozen_set:
        word_matched_set = \
            {word for word in word_frozen_set if char in word}              
        comb_matched_dict[char].update(word_matched_set)   

# 2 chars
    comb_set = get_char_combination_set(char_frozen_set,2)      
    for comb in comb_set:
        comb_matched_dict[comb]=set()
        comb_matched_dict[comb] = \
            comb_matched_dict[comb[0]].union(comb_matched_dict[comb[1]])
# 3 chars
    comb_set = get_char_combination_set(char_frozen_set,3)      
    for comb in comb_set:
        comb_matched_dict[comb]=set()
        comb_matched_dict[comb] = \
            comb_matched_dict[comb[0]+comb[1]].union(comb_matched_dict[comb[2]])
# 5 chars
    comb_set = get_char_combination_set(char_frozen_set,5)      
    for comb in comb_set:
        comb_matched_dict[comb]=set()
        comb_matched_dict[comb] = \
            comb_matched_dict[comb[0]+comb[1]+comb[2]].union(comb_matched_dict[comb[3]+comb[4]])

    return comb_matched_dict



@timing
def main_unmatched(char_frozen_set,word_frozen_set):

    comb_unmatched_dict = dict()
    for char in char_frozen_set:
        comb_unmatched_dict[char]=set()
    
# 1 char
    for char in char_frozen_set:
        word_unmatched_set = \
            {word for word in word_frozen_set if char not in word}        
        comb_unmatched_dict[char].update(word_unmatched_set)   
# 2 chars
    comb_set = get_char_combination_set(char_frozen_set,2)      
    for comb in comb_set:
        comb_unmatched_dict[comb]=set()
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]].intersection(comb_unmatched_dict[comb[1]])
# 3 chars
    comb_set = get_char_combination_set(char_frozen_set,3)      
    for comb in comb_set:
        comb_unmatched_dict[comb]=set()
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]+comb[1]].intersection(comb_unmatched_dict[comb[2]])
# 5 chars
    comb_set = get_char_combination_set(char_frozen_set,5)      
    for comb in comb_set:
        comb_unmatched_dict[comb]=set()
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]+comb[1]+comb[2]].intersection(comb_unmatched_dict[comb[3]+comb[4]])
    return comb_unmatched_dict

@timing
def main_unmatched(char_frozen_set,word_frozen_set):

    comb_unmatched_dict = dict()
    for char in char_frozen_set:
        comb_unmatched_dict[char]=set()
    
# 1 char
    for char in char_frozen_set:
        word_unmatched_set = \
            {word for word in word_frozen_set if char not in word}        
        comb_unmatched_dict[char].update(word_unmatched_set)   
# 2 chars
    comb_set = get_char_combination_set(char_frozen_set,2)      
    for comb in comb_set:
        comb_unmatched_dict[comb]=set()
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]].intersection(comb_unmatched_dict[comb[1]])
# 3 chars
    comb_set = get_char_combination_set(char_frozen_set,3)      
    for comb in comb_set:
        comb_unmatched_dict[comb]=set()
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]+comb[1]].intersection(comb_unmatched_dict[comb[2]])
# 5 chars
    comb_set = get_char_combination_set(char_frozen_set,5)      
    for comb in comb_set:
        comb_unmatched_dict[comb]=set()
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]+comb[1]+comb[2]].intersection(comb_unmatched_dict[comb[3]+comb[4]])
    return comb_unmatched_dict


### SHORTER CODE ###

@timing
def main_unmatched_shorter(char_frozen_set,word_frozen_set):

    comb_unmatched_dict = dict()
    for char in char_frozen_set:
        comb_unmatched_dict[char]=set()
    
# 1 char
    for char in char_frozen_set:
        word_unmatched_set = \
            {word for word in word_frozen_set if char not in word}        
        comb_unmatched_dict[char].update(word_unmatched_set)   

# 5 chars
    comb_set = get_char_combination_set(char_frozen_set,5)      
    for comb in comb_set:
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]]\
                .intersection(comb_unmatched_dict[comb[1]]) \
                .intersection(comb_unmatched_dict[comb[2]]) \
                .intersection(comb_unmatched_dict[comb[3]]) \
                .intersection(comb_unmatched_dict[comb[4]])
    return comb_unmatched_dict






@timing
def main_unmatched_no_empty_sets(char_frozen_set,word_frozen_set):

    comb_unmatched_dict = dict()
    for char in char_frozen_set:
        comb_unmatched_dict[char]=set()
    
# 1 char
    for char in char_frozen_set:
        word_unmatched_set = \
            {word for word in word_frozen_set if char not in word}        
        comb_unmatched_dict[char].update(word_unmatched_set)   
# 2 chars
    comb_set = get_char_combination_set(char_frozen_set,2)      
    for comb in comb_set:
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]].intersection(comb_unmatched_dict[comb[1]])
# 3 chars
    comb_set = get_char_combination_set(char_frozen_set,3)      
    for comb in comb_set:
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]+comb[1]].intersection(comb_unmatched_dict[comb[2]])
# 5 chars
    comb_set = get_char_combination_set(char_frozen_set,5)      
    for comb in comb_set:
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]+comb[1]+comb[2]].intersection(comb_unmatched_dict[comb[3]+comb[4]])
    return comb_unmatched_dict



@timing
def main_unmatched_5_steps(char_frozen_set,word_frozen_set):

    comb_unmatched_dict = dict()
    for char in char_frozen_set:
        comb_unmatched_dict[char]=set()
    
# 1 char
    for char in char_frozen_set:
        word_unmatched_set = \
            {word for word in word_frozen_set if char not in word}        
        comb_unmatched_dict[char].update(word_unmatched_set)   
# 2 chars
    comb_set = get_char_combination_set(char_frozen_set,2)      
    for comb in comb_set:
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]]\
                .intersection(comb_unmatched_dict[comb[1]])
# 3 chars
    comb_set = get_char_combination_set(char_frozen_set,3)      
    for comb in comb_set:
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]+comb[1]]\
                .intersection(comb_unmatched_dict[comb[2]])

# 4 chars
    comb_set = get_char_combination_set(char_frozen_set,4)      
    for comb in comb_set:
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]+comb[1]+comb[2]]\
                .intersection(comb_unmatched_dict[comb[3]])

# 5 chars
    comb_set = get_char_combination_set(char_frozen_set,5)      
    for comb in comb_set:
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]+comb[1]+comb[2]+comb[3]]\
                .intersection(comb_unmatched_dict[comb[4]])
   
    return comb_unmatched_dict



def main():

    #char_frozen_set = frozenset(['a', 'b', 'c'])
    #char_frozen_set = frozenset("abcdefg")
    char_frozen_set = frozenset(string.ascii_lowercase)
    char_list = string.ascii_lowercase

    
    word_frozen_set = frozenset(['auto', 'bus', 'step'])
    #word_frozen_set = frozenset(['auto', 'bus', 'step','bike'])
    #word_frozen_set = frozenset(get_wordlist_from_file('words.txt')[0:10])
    #word_frozen_set = frozenset(get_wordlist_from_file('words.txt')[0:100])
    #word_frozen_set = frozenset(get_wordlist_from_file('words.txt')[0:1_000])
    #word_frozen_set = frozenset(get_wordlist_from_file('words.txt')[0:10_000])
    #word_frozen_set = frozenset(get_wordlist_from_file('words.txt'))

    #main_matched(char_frozen_set, word_frozen_set)
    #main_unmatched_shorter(char_frozen_set, word_frozen_set)
    #main_unmatched(char_frozen_set, word_frozen_set)
    #main_unmatched_no_empty_sets(char_frozen_set, word_frozen_set)
    #main_unmatched_5_steps(char_frozen_set, word_frozen_set)
    #print()


if __name__ == '__main__':
    main()