from string import ascii_lowercase
from pprint import pprint
from functions import *

@timing
def main():

    char_list = ascii_lowercase
    word_list = get_wordlist_from_file("words.txt")

    comb_1_dict = dict()

    for char in char_list:
        comb_1_dict[char] = sum(1 for word in word_list if char in word)

    char_list_sorted = \
        sorted(comb_1_dict.items(), key=lambda item: item[1], reverse = True)

    best_estimate = ''.join([char for char, _ in char_list_sorted[-5:]])
    #print(f"{best_estimate=}")
    best_estimate_count = \
        sum(1 for word in word_list if any(char in word for char in best_estimate))

    length = len(char_list_sorted)
    reduced_dict = dict()

    for i in range(0,length-4):
        char_i = char_list_sorted[i][0]
        count = char_list_sorted[i][1]
        comb = char_i
        if count > best_estimate_count : continue
        #reduced_dict[comb] = count

        for j in range(i+1,length-3):
            char_j = char_list_sorted[j][0]
            comb = char_i + char_j
            count = sum(1 for word in word_list if any(char in word for char in comb))
            if count > best_estimate_count : continue
            #reduced_dict[comb] = count
        
            for k in range(j+1,length-2):
                char_k = char_list_sorted[k][0]
                comb = char_i + char_j + char_k
                count = sum(1 for word in word_list if any(char in word for char in comb))
                if count > best_estimate_count : continue
                #reduced_dict[comb] = count

                for l in range(k+1,length-1):
                    char_l = char_list_sorted[l][0]
                    comb = char_i + char_j + char_k + char_l
                    count = sum(1 for word in word_list if any(char in word for char in comb))
                    if count > best_estimate_count : continue
                    #reduced_dict[comb] = count


                    for m in range(l+1,length):
                        char_m = char_list_sorted[m][0]
                        comb = char_i + char_j + char_k + char_l + char_m
                        count = sum(1 for word in word_list if any(char in word for char in comb))
                        if count > best_estimate_count : continue
                        print(f"{comb}:{count}")
                        reduced_dict[comb] = count
                        
    pprint(reduced_dict)
    min_comb = min(reduced_dict, key=reduced_dict.get)
    print(f"lowest combination = {min_comb}")
        
if __name__ == '__main__':
    main()