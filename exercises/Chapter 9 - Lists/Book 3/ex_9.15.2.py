from datetime import time, datetime

def is_anagram(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)


#goede manier
with open("../../Chapter 10 - dicts/Book 3/words.txt", "r") as f:
    words = f.read().split("\n")


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
    w = [word for word in w if "s" in word]
    w = [word for word in w if "a" in word]
    w = [word for word in w if "k" in word]
    w = [word for word in w if "e" in word]

    return [word for word in w if is_anagram(word, "takes")]

def method_4():
    pass

def method_5():
    w = [word for word in words if len(word) == 5]
    w = [word for word in w if "t" in word]
    w = [word for word in w if "s" in word]
    w = [word for word in w if "a" in word]
    w = [word for word in w if "k" in word]
    w = [word for word in w if "e" in word]

def method_6():

    i = "takes"

    w = [word for word in words if len(word) == 5]

    for a in i:
        w = [word for word in w if a in word]

    return [word for word in w if sorted(w) == "aeskt"]



if __name__ == "__main__":
    # start = datetime.now()
    # for _ in range(100):
    #     method_1()
    # end = datetime.now()
    # print(end - start)

    # start = datetime.now()
    # for _ in range(100):
    #     method_2()
    # end = datetime.now()
    # print(end - start)

    # start = datetime.now()
    # for _ in range(100):
    #     method_3()
    # end = datetime.now()
    # print(end - start)

    # start = datetime.now()
    # for _ in range(100):
    #     method_4()
    # end = datetime.now()
    # print(end - start)

    # start = datetime.now()
    # for _ in range(100):
    #     method_5()
    # end = datetime.now()
    # print(end - start)

    start = datetime.now()
    for _ in range(100):
        method_6()
    end = datetime.now()
    print(end - start)


#slechte manier voor 8 en 9
# f = open("words.txt", "r")
# words = f.read().split("\n")
# f.close()

