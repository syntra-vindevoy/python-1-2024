# %%
import os

# %%
script_dir = os.path.dirname(__file__)
file_name = "words.txt"
file_path = os.path.join(script_dir, file_name)

with open(file_path, "r") as f:
    word_list = f.read().split()


# %%
def word_distance(word1, word2):
    zip_difference = 0
    for pair in zip(word1, word2):
        if pair[0] != pair[1]:
            zip_difference += 1
    return zip_difference


# %%


def has_one_char_less(word1, word2):
    found_new_char = False
    if len(word1) != len(word2) - 1:
        return False
    for i in range(len(word1)):
        if found_new_char == False:
            if word1[i] != word2[i]:
                found_new_char = True
        if found_new_char == True:
            if word1[i] == word2[i + 1]:
                continue
            else:
                return False
    return True


print(has_one_char_less("hello", "hxllo"))
print(has_one_char_less("ample", "amples"))
print(has_one_char_less("kitten", "kietten"))
print(has_one_char_less("ab", "xyz"))

# %%


def word_list_by_char_count(word_list, char_count):
    return [word for word in word_list if len(word) == char_count]

def get_combo_list(this_word_list, next_word_list, combo_list):

this_word_list = word_list_by_char_count(word_list, 2)
next_word_list = word_list_by_char_count(word_list, 3)





# %%
