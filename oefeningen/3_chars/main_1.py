from itertools import combinations


char_list = list("abcd")
word_list = ["ab", "bc", "cd", "dbcd", "da", "bdc", "a"]
"""
"""
alphabet = char_list
print(f"{alphabet=}")
words = word_list
print(f"{words=}")

char_dict_1_char = {char: 0 for char in char_list}
char_dict_2_char = {"".join(combo): 0 for combo in combinations(char_list, 2)}
char_dict_3_char = {"".join(combo): 0 for combo in combinations(char_list, 3)}

for char in char_list:
    char_dict_1_char[char] = sum(1 for word in word_list if char in word)

chars = char_dict_1_char
print(f"{chars=}")


length = len(char_list)

for i in range(0, length - 2):
    char_i = char_list[i]
    for j in range(i + 1, length - 1):
        char_j = char_list[j]
        for k in range(j + 1, length):
            char_k = char_list[k]
            comb = char_i + char_j + char_k
            count = sum(1 for word in word_list if any(char in word for char in comb))
            char_dict_3_char[comb] = count

combinations = char_dict_3_char
print(f"{combinations=}")
