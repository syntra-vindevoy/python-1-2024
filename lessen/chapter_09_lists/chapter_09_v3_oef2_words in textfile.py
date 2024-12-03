import sys
from datetime import datetime
import os
import sys


def is_anagram(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)


def get_wordlist_from_file(file: str):
    script_dir = os.path.dirname(__file__)
    file_name = "words.txt"
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, "r") as f:
        words = f.read().split("\n")
    return words


words = get_wordlist_from_file("words.txt")

print("number of words: ", len(words))


def method_1():
    anagrams = []
    for word in words:
        if is_anagram(word, "takes"):
            anagrams.append(word)

    return anagrams


### classic method, do not use anymore
# f = open("words.txt", "r")
# words = f.read().split("\n")
# f.close()


def method_2():
    return [word for word in words if is_anagram(word, "takes")]


def method_3():
    w = [word for word in words if "t" in word]
    w = [word for word in w if "s" in word]
    w = [word for word in w if "k" in word]
    w = [word for word in w if "e" in word]
    w = [word for word in w if "a" in word]

    return [word for word in w if is_anagram(word, "takes")]


def method_4():
    w = [word for word in words if len(word) == 5]

    return [word for word in w if is_anagram(word, "takes")]


def method_5():
    w = [word for word in words if len(word) == 5]
    w = [word for word in w if "t" in word]
    w = [word for word in w if "s" in word]
    w = [word for word in w if "k" in word]
    w = [word for word in w if "e" in word]
    w = [word for word in w if "a" in word]

    return [word for word in w if is_anagram(word, "takes")]


def method_6():
    w = [word for word in words if len(word) == 5]
    w = [word for word in w if "t" in word]
    w = [word for word in w if "s" in word]
    w = [word for word in w if "k" in word]
    w = [word for word in w if "e" in word]
    w = [word for word in w if "a" in word]

    return [word for word in w if sorted(w) == "aekst"]


def method_7():
    i = "takes"
    w = [word for word in words if len(word) == len(i)]

    for a in i:
        w = [word for word in w if a in word]

    return [word for word in w if sorted(w) == "aekst"]


if __name__ == "__main__":

    functions = [
        method_1,
        method_2,
        method_3,
        method_4,
        method_5,
        method_6,
        method_7,
    ]
    for func in functions:
        start = datetime.now()
        for _ in range(100):
            func()
        end = datetime.now()
        print(end - start)

    sys.exit()

    for i in range(1, 8):
        func = globals()[f"method_{i}"]  # globals returns all the global variables
        start = datetime.now()
        for _ in range(100):
            func()
        end = datetime.now()
        print(f"method_{i} took {end - start}")

#####
