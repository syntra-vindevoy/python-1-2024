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


    char_list = list(ALPHABET.value)

    # 1 char
    length = len(char_list)

    remaining_words_set_start = word_set     

    for i in range(0,length-4):
        char_i = char_list[i]
        set_i = set(word for word in remaining_words_set_start if char_i in word)
        combination_dict_1_chars[char_i] = set_i
        remaining_words_set_after_i = word_set - set_i

        for j in range(1,length-3):
            char_j = char_list[j]
            set_j = set(word for word in remaining_words_set_after_i if char_j in word)
            combination_dict_2_chars[char_i+char_j] = set_j
            remaining_words_set_after_j = remaining_words_set_after_i - set_j

            for k in range(2,length-2):
                char_k = char_list[k]
                set_k = set(word for word in remaining_words_set_after_j if char_j in word)
                combination_dict_3_chars[char_i+char_j+char_k] = set_k
                remaining_words_set_after_k = remaining_words_set_after_j - set_k

                for l in range(3,length-1):
                    char_l = char_list[l]
                    set_l = set(word for word in remaining_words_set_after_k if char_l in word)
                    combination_dict_4_chars[char_i+char_j+char_k+char_l] = set_l
                    remaining_words_set_after_l = remaining_words_set_after_k - set_l

                    for m in range(4,length):
                        char_m = char_list[m]
                        set_m = set(word for word in remaining_words_set_after_l if char_m in word)
                        combination_dict_5_chars[char_i+char_j+char_k+char_l] = set_m


    #pprint(combination_dict_1_chars['b'])
    #pprint(combination_dict_2_chars['ab'])
    pprint(combination_dict_5_chars['abcde'])

            

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