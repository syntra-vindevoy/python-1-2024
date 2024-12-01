import sys
from datetime import datetime
import time
import os


opgave = """
This question is based on a Puzzler that was broadcast on the radio program Car Talk (http://www.cartalk.com/content/puzzlers):
Give me a word with three consecutive double letters. I’ll give you a couple of words that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it would work. But there is a word that has three consecutive pairs of letters and to the best of my knowledge this may be the only word. Of course there are probably 500 more but I can only think of one. What is the word?
Write a program to find it. Solution: https://thinkpython.com/code/cartalk1.py.
"""


def get_wordlist_from_file(file: str):
    script_dir = os.path.dirname(__file__)
    file_name = "words.txt"
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, "r") as f:
        words = f.read().split("\n")
    return words


def has_3_consecutive_matching_chars(word):
    previous_char = ""
    streak = 1
    streak_max = 0
    for char in word:
        if char == previous_char:
            streak += 1
        if streak > streak_max:
            streak_max = streak
        else:
            streak = 1
        previous_char = char
    return streak_max >= 3


def run_asserts():
    assert has_3_consecutive_matching_chars("moehahahhh")

    words_true = ["moehahahhh", "ahaaa"]
    words_false = ["moehaha", "aha"]
    for word in words_true:
        assert has_3_consecutive_matching_chars(word)
    for word in words_false:
        assert has_3_consecutive_matching_chars(word) == False
    """
    """


def get_runtime_as_string(start_time: datetime, end_time: datetime) -> str:
    runtime = end_time - start_time
    seconds = runtime.total_seconds()
    return f"{seconds=:.5f}"


def main():
    run_tests = False
    start_time = datetime.now()

    matching_words = []
    wordlist = get_wordlist_from_file("words.txt")

    start_asserts = datetime.now()
    if run_tests:
        run_asserts()
    end_asserts = datetime.now()

    for word in wordlist:
        if has_3_consecutive_matching_chars(word):
            matching_words.append(word)

    end_time = datetime.now()

    ljust_length = 10
    print(
        "Asserts:".ljust(ljust_length)
        + get_runtime_as_string(start_asserts, end_asserts)
    )
    print("Finished:".ljust(ljust_length) + get_runtime_as_string(start_time, end_time))

    print(matching_words)

    sys.exit()


if __name__ == "__main__":
    main()
