# %%
import os
from icecream import ic
from itertools import combinations

# %%
script_dir = os.path.dirname(__file__)
file_name = "words.txt"
file_path = os.path.join(script_dir, file_name)

with open(file_path, "r") as f:
    word_list = f.read().split()


def word_distance(word1, word2):
    zip_difference = 0
    for pair in zip(word1, word2):
        if pair[0] != pair[1]:
            zip_difference += 1
    return zip_difference


word_dict = {}
for word in word_list:
    sorted_word = tuple(sorted(word))
    pass
    if sorted_word not in word_dict:
        word_dict[sorted_word] = list()
    word_dict[sorted_word].append(word)

# %%

anagrams = {k: v for k, v in word_dict.items() if len(v) > 1}
# %%

for key, value_list in anagrams.items():
    for word1, word2 in combinations(value_list, 2):
        if word_distance(word1, word2) == 2:
            print(word1, word2)
