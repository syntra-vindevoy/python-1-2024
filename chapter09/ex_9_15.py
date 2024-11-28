from datetime import datetime
from multiprocessing.util import is_abstract_socket_namespace


def is_annagram(woord_a, woord_b):
    return sorted(woord_a) == sorted(woord_b)

with open("words.txt", "r") as f:
    words = f.read().split("\n")

print("number of words: ", len(words))

def method_1():
    anagrams = []
    for word in words:
        if is_annagram(word, "takes"):
            anagrams.append(word)

    return anagrams

def method_2():
    return [word for word in words if is_annagram(word, "takes")]

def method_3():
    w = [word for word in words if "t" in word]
    w = [word for word in w if "s" in word]
    w = [word for word in w if "k" in word]
    w = [word for word in w if "e" in word]
    w = [word for word in w if "a" in word]

    return [word for word in w if is_annagram(word,"takes")]

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

#print(words)
#print(type(words))