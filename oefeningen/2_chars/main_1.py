from itertools import combinations


char_list = list("abcd")
word_list = "ab cb cd".split()

char_list = list("abcde")
word_list = "ab cbe cd cde".split()
word_list = "ae cbe cd bcd".split()
words_list = ["ae", "abe", "cd", "bcd"]

char_list = list("abcd")
word_list = ["ab", "cb", "cd", "ad"]
word_list = ["ab", "ac", "bc", "bd", "cd"]
word_list = ["ab", "bc", "cd", "da"]
word_list = ["ab", "bc", "cd", "de", "ef"]

char_list = list("abcd")
word_list = ["a", "b", "c"]
word_list = ["ab", "bc", "cd", "da"]
"""
"""

print(f"{char_list=}")
print(f"{word_list=}")

char_dict_1_char = {char: 0 for char in char_list}
char_dict_2_char = {"".join(combo): 0 for combo in combinations(char_list, 2)}

for char in char_list:
    char_dict_1_char[char] = sum(1 for word in word_list if char in word)
print(f"{char_dict_1_char=}")


length = len(char_list)

for i in range(0, length - 1):
    char_i = char_list[i]
    for j in range(i + 1, length):
        char_j = char_list[j]
        comb = char_i + char_j
        count = sum(1 for word in word_list if any(char in word for char in comb))
        char_dict_2_char[comb] = count

print(f"{char_dict_2_char=}")
