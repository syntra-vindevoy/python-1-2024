from constants import *
from functions import *

from pprint import pprint

@timing
def main():
    file_name = "words.txt"
    word_set = set(get_wordlist_from_file(file_name))

    combination_dict_1_chars = {}
    combination_dict_2_chars = {}
    combination_dict_3_chars = {}
    combination_dict_4_chars = {}
    combination_dict_5_chars = {}

    print(ALPHABET.value)

    new_word_set = word_set

    char_list = list(ALPHABET.value)

    #for i in range(0,len(char_list)):
    for i in range(0,1):
        char_1 = char_list[i]
        this_word_set = set(word for word in new_word_set if char_1 in word)
        combination_dict_1_chars[char_1] = this_word_set
        new_word_set = new_word_set - this_word_set


              
    pprint (combination_dict_1_chars)
            

if __name__ == "__main__":

    main()

'''

char_1 = char_list[i] #A
this_word_set = set(word for word in new_word_set if char_1 in word)
combination_dict_1_char[char_1] = this_word_set
new_word_set = new_word_set - this_word_set

for j in range(i+1,len(char_list)):
    char_2 = char_list[j]

'''
'''






contains_a = any('a' in comb for comb in combination_dict['b'])
print(f"Combinations with 'a' in 'b' combinations: {contains_a}")
'''