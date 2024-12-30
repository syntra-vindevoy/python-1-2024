from functions import *
import string
from icecream import ic


def get_sorted_word_list(word_list):
    return [(sorted(set(word)),(set())) for word in word_list]

@timing
def main():
    word_list = get_wordlist_from_file("words.txt")
    char_list = string.ascii_lowercase
    comb_list = get_char_combination_set(char_list, 5)

    sorted_word_list = get_sorted_word_list(word_list)
    #ic(sorted_word_list[:10])


    comb_dict = dict()
    for comb in comb_list:
        comb_dict[comb] = 0


    for i in range(len(char_list)):
        char = char_list[i]

        matching_comb_list = \
            [comb for comb in comb_list 
             if char in comb]
        
        matching_word_list_all = \
            [word for word in sorted_word_list 
            if char in word[0]]
        
        for comb in matching_comb_list:
            sub_matching_word_list_all = \
                [word for word in matching_word_list_all
                 if not any(sub_char in word[1] for sub_char in comb)]
            
            comb_dict[comb] += len(sub_matching_word_list_all)


    ic(sorted_word_list[:10])
    ic([f"{comb}:{comb_dict[comb]}" for comb in comb_dict if 'abcd' in comb])

    min_comb = min(comb_dict, key=comb_dict.get)
    print(f"The combination with the least counts is {min_comb} with {comb_dict[min_comb]} counts")

if __name__ == "__main__":
    main()