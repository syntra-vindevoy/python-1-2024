from icecream import ic

import os


def get_file_content(file: str):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file} does not exist at {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        words = f.read()
    return words


def most_frequent_characters(string: str):
    def value_counts(string):
        counter = {}
        for letter in string:
            if letter not in counter:
                counter[letter] = 1
            else:
                counter[letter] += 1
        return counter

    def second_element(t):
        return t[1]

    return sorted(value_counts(string).items(), key=second_element, reverse=True)


import string

character_list = string.ascii_lowercase

characters = most_frequent_characters(get_file_content("dracula.txt").lower())
for key, value in characters:
    if key in character_list:
        print(f"{key}:{value}")
