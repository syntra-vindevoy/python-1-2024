
from functions import *
from collections import defaultdict

@timing
def main():
    ic.disable()
    char_frozen_set = frozenset(['a', 'b', 'c'])
    char_frozen_set = frozenset("abcdefg")
    char_frozen_set = frozenset(string.ascii_lowercase)

    comb_matched_dict = dict()
    for char in char_frozen_set:
        comb_matched_dict[char]=set()

    comb_unmatched_dict = dict()
    for char in char_frozen_set:
        comb_unmatched_dict[char]=set()
    


    ic(comb_matched_dict)
    word_frozen_set = frozenset(['auto', 'bus', 'step'])
    word_frozen_set = frozenset(get_wordlist_from_file('words.txt')[0:10])
    #word_frozen_set = frozenset(get_wordlist_from_file('words.txt'))
    ic(word_frozen_set)
    
# 1 char
    for char in char_frozen_set:
        ic(char)
        word_matched_set = \
            {word for word in word_frozen_set if char in word}      
        ic(word_matched_set)

        word_unmatched_set = \
            {word for word in word_frozen_set if char not in word}      
        ic(word_unmatched_set)
        
        comb_matched_dict[char].update(word_matched_set)   
        comb_unmatched_dict[char].update(word_unmatched_set)   
    ic(comb_matched_dict)
    ic(comb_unmatched_dict)
# 2 chars
    comb_set = get_char_combination_set(char_frozen_set,2)      
    ic(comb_set)
    for comb in comb_set:
        ic(comb)
        comb_matched_dict[comb]=set()
        comb_unmatched_dict[comb]=set()
        comb_matched_dict[comb] = \
            comb_matched_dict[comb[0]].union(comb_matched_dict[comb[1]])
        ic(comb_matched_dict)
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]].intersection(comb_unmatched_dict[comb[1]])
        ic(comb_unmatched_dict)
# 3 chars
    comb_set = get_char_combination_set(char_frozen_set,3)      
    ic(comb_set)
    for comb in comb_set:
        ic(comb)
        comb_matched_dict[comb]=set()
        comb_unmatched_dict[comb]=set()
        comb_matched_dict[comb] = \
            comb_matched_dict[comb[0]+comb[1]].union(comb_matched_dict[comb[2]])
        ic(comb_matched_dict)
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]+comb[1]].intersection(comb_unmatched_dict[comb[2]])
        ic(comb_unmatched_dict)
# 5 chars
    comb_set = get_char_combination_set(char_frozen_set,5)      
    ic(comb_set)
    for comb in comb_set:
        ic(comb)
        comb_matched_dict[comb]=set()
        comb_unmatched_dict[comb]=set()
        comb_matched_dict[comb] = \
            comb_matched_dict[comb[0]+comb[1]+comb[2]].union(comb_matched_dict[comb[3]+comb[4]])
        ic(comb_matched_dict)
        comb_unmatched_dict[comb] = \
            comb_unmatched_dict[comb[0]+comb[1]+comb[2]].intersection(comb_unmatched_dict[comb[3]+comb[4]])
        ic(comb_unmatched_dict)
    ic.enable()
    ic(comb_matched_dict)
    ic(comb_unmatched_dict)


if __name__ == '__main__':
    main()