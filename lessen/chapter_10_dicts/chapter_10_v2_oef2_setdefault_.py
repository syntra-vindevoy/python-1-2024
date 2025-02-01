"""
Read the documentation of the dictionary method setdefault and use it to write a more concise version of invert_dict. Solution: https://thinkpython.com/code/invert_dict.py.
"""

import os


def get_wordlist_from_file(file: str):
    script_dir = os.path.dirname(__file__)
    file_name = "words.txt"
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, "r") as f:
        words = f.read().split()

    word_dict = {word: 0 for word in words}
    return word_dict


def invert_dict(original_dict):
    # Initialize an empty dictionary to store the inverted dictionary
    inverse = {}

    """
    for key in original_dict:
        val = original_dict[key]
        if val not in inverse:
            inverse[val] = []  # Initialize the list if the key does not exist
        inverse[val].append(key)  # Append the key to the list

        # https://github.com/AllenDowney/ThinkPython2/blob/master/code/invert_dict.py
    """

    for key in original_dict:  # Iterate over each key in the original dictionary
        val = original_dict[key]
        inverse.setdefault(val, []).append(key)
    return inverse  # Return the inverted dictionary
