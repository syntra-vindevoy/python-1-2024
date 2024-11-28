from datetime import datetime
from chap09_is_anagram import is_anagram

###Classic way, but bad way, because you have to close the file at the end
#f = open("words.txt", "r")
#words = f.read().split("\n")
#f.close()

#Correct way, because the context manager "with" already closes the file for you at the end
with open("words.txt", "r") as f:
    words = f.read().split("\n")

#print(words)
#print(type(words))

for word in words:
    if is_anagram(word, "takes"):
        print(word)

def method_1():
    anagrams = []
    for word in words:
        if is_anagram(word, "takes"):
            anagrams.append(word)

    return anagrams


def method_2():
    return [word for word in words if is_anagram(word, "takes")]


def method_3():
    w = [word for word in words if "t" in word]
    w = [word for word in w if "a" in word]
    w = [word for word in w if "k" in word]
    w = [word for word in w if "e" in word]
    w = [word for word in w if "s" in word]

    return [word for word in w if is_anagram(word, "takes")]


def method_4():
    w = [word for word in words if len(word) == 5]

    return [word for word in w if is_anagram(word, "takes")]


def method_5():
    w = [word for word in words if len(word) == 5]
    w = [word for word in w if "t" in word]
    w = [word for word in w if "a" in word]
    w = [word for word in w if "k" in word]
    w = [word for word in w if "e" in word]
    w = [word for word in w if "s" in word]

    return [word for word in w if is_anagram(word, "takes")]


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