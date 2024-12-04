def is_anagram(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)


def is_palindrome(word: str) -> bool:
    return word == word[::-1]


def is_voodoo(word: str) -> bool:
    return word[1:] == word[1:][::-1]


assert is_voodoo("voodoo")
assert is_voodoo("voo")
assert not is_voodoo("oov")

steden = ["Brussel", "Oudenaarde", "Zottegem", "Opwijk", "Sint-Niklaas", "Kortrijk", "Deinze", "Gent", "Aalst",
          "Erpe-Mere", "Ninove"]

# for stad in steden[::-1]:
#     print("Ik controleer", stad)
#     begin = stad[0].lower()
#
#     if begin in "aeuioy":
#         print("Ik verwijder ", stad)
#         steden.remove(stad)

steden = [stad for stad in steden if stad[0].lower() not in "aeuioy"]

print(steden)

with open("words.txt", "r") as f:
    words = f.read()

s = 0
for word in words:
    s += len(word.strip())

print(s)

with open("words.txt", "r") as f:
    words = f.read().splitlines()

    s = "".join(word for word in words)
    print(len(s))

with open("words.txt", "r") as f:
    words = f.read().splitlines()

    s = sum([len(w) for w in words])
    print(s)

with open("words.txt", "r") as f:
    words = f.read()

words = words.replace("\n", "")
print(len(words))

with open("words.txt", "r") as f:
    words = f.read()
    print(len(words) - words.count("\n"))

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
