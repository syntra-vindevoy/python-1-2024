# exercise 10.1 from book thinkpython
from datetime import datetime

t= [[1,2], [4,5,6], [3]]
def nested_sum(list):
    return sum(sum(sublist) for sublist in list)

print(nested_sum(t))
print (t[2])

# exercise 10.2 from book thinkpython

t2 = [1,2,3]
def cumsum(list2):
    result = []
    current_sum = 0
    for num in list2:
        current_sum += num
        result.append(current_sum)
    return result
print(cumsum(t2))

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
    return [word for word in words if is_anagram(word, 'takes')]

def method_3():
    w = [word for word in words if "t" in word]
    w = [word for word in w if "s" in word]
    w = [word for word in w if "k" in word]

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

# for word in words:
#     if is_anagram(word, "takes"):
#         print(word)
#
# print (words)
# print(type(words))

# file = open("words.txt", "r")       # niet de manier voor het openen van files
# words = file.read().split("\n")
# file.close()


