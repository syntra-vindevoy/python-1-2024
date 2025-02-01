import string
from icecream import ic
import os


def rotate_word(word, n, chars):
    n = n % 26
    return "".join([chars[chars.index(i) + n] for i in word])


def get_base_position(word, chars):
    position_list = [chars.index(i) for i in word]
    return map(lambda x: x - position_list[0], position_list)


chars = string.ascii_lowercase * 2

file_path = os.path.join(os.path.dirname(__file__), "words.txt")
with open(file_path, "r") as file:
    word_list = file.read().splitlines()

positional_dict = {}
for word in word_list:
    position = tuple(get_base_position(word, chars))
    if position not in positional_dict:
        positional_dict[position] = [word]
    else:
        positional_dict[position].append(word)

positional_dict = {
    key: value for key, value in positional_dict.items() if len(value) > 1
}

ic(positional_dict)
