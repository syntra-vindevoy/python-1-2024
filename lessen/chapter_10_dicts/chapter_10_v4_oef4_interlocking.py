"""
A word is "interlocking" if we can split it into two words by taking alternating letters. For example, "schooled" is an interlocking word because it can be split into "shoe" and "cold".

To select alternating letters from a string, you can use a slice operator with three components that indicate where to start, where to stop, and the "step size" between the letters.

In the following slice, the first component is 0, so we start with the first letter. The second component is None, which means we should go all the way to the end of the string. And the third component is 2, so there are two steps between the letters we select.

Write a function called is_interlocking that takes a word as an argument and returns True if it can be split into two interlocking words.

"""

# %%

import os


def get_wordlist_from_file(file: str):
    script_dir = os.path.dirname(__file__)
    file_name = "words.txt"
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, "r") as f:
        words = f.read().split("\n")
    return words


def is_interlocking(word: str, words: list[str]) -> bool:
    word_1 = word[0::2]
    word_2 = word[1::2]
    return (word_1 in words) and (word_2 in words)


words = get_wordlist_from_file("words.txt")
print(is_interlocking("schooled", words))

pass
# %%
