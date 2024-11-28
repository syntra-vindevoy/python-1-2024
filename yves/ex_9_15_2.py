import sys
from datetime import datetime


def is_anagram(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)

with open("words.txt", "r") as f:
    words = f.read().split("\n")

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
    start = datetime.now()
    for _ in range(100):
        method_1()
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    for _ in range(100):
        method_2()
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    for _ in range(100):
        method_3()
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    for _ in range(100):
        method_4()
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    for _ in range(100):
        method_5()
    end = datetime.now()
    print(end - start)


    start = datetime.now()
    for _ in range(100):
        method_6()
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    for _ in range(100):
        method_7()
    end = datetime.now()
    print(end - start)
