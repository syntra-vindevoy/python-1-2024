from datetime import datetime
# exercise 10.3 from book thinkpython

t3 = [1, 2, 3, 4]
def middle(list3):
    return list3 [1:-1]
print(middle(t3))

# exercise 9.15 from thinkpython online
def is_anagram(word1 :str, word2 :str) -> bool:
    return sorted(word1) == sorted(word2)
#
with open("words.txt", "r") as file:    # de manier voor het openen van een file
    words = file.read().split("\n")
#
# print ("number of words" , len(words))

def method_1():
    anagrams = []
    for word in words:
        if is_anagram(word, 'takes'):
            anagrams.append(word)
    return anagrams

def method_2():
    return [word for word in words if is_anagram(word, 'takes')]  # -> list comprehension opzoeken

def method_3():
    w = [word for word in words if "t" in word]
    w = [word for word in w if "s" in word]
    w = [word for word in w if "k" in word]
    w = [word for word in w if "e" in word]
    w = [word for word in w if "a" in word]

    return [word for word in w if is_anagram(word,'takes')]

def method_4():
    w = [word for word in words if len(word) == 5 ]
    return [word for word in w if is_anagram(word,'takes')]

def method_5():
    w = [word for word in words if len(word) == 5 ]
    w = [word for word in w if "t" in word]
    w = [word for word in w if "s" in word]
    w = [word for word in w if "k" in word]
    w = [word for word in w if "e" in word]
    w = [word for word in w if "a" in word]

    return [word for word in w if is_anagram(word,'takes')]

if __name__ == "__main__":
    start = datetime.now()
    for _ in range(5):
        method_1()
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    for _ in range(5):
        method_2()
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    for _ in range(5):
        method_3()
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    for _ in range(5):
        method_4()
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    for _ in range(5):
        method_5()
    end = datetime.now()
    print(end - start)
# for word in words:
#     if is_anagram(word, "takes"):
#         print(word)
#
# print (words)
# print(type(words))

# file = open("words.txt", "r")       # niet de manier voor het openen van files
# words = file.read().split("\n")
# file.close()
