from functions import *
import string

word_list = get_wordlist_from_file("words.txt")
char_list = string.ascii_lowercase
comb_list = get_char_combination_set(char_list, 5)

word_list = sorted(word_list)
char_list = sorted(char_list)
comb_list = sorted(comb_list)

word_set = set(word_list)

word_list_long = \
    [char for char in char_list]
    

