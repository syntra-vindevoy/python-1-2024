from datetime import datetime

from chap09_is_anagram import is_anagram

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


###Classic way, but bad way, because you have to close the file at the end
#f = open("words.txt", "r")
#words = f.read().split("\n")
#f.close()

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