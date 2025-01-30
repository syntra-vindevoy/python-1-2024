
# d = {}
#
# d["name"] = "John"
# d["0"] = "jkl"
# d["names"] = [ "John", "Jane"]
#
# # print(d)
# # print(d["name"])
# # print(len(d)) #lengt van dict
#
# lst = [1,2,3, 4,5,6]
#
# d = {i:list[i] for i in range(len(lst))}
#
# print(d)
#
# print(d.keys())
# print(d.values())

from Lib.test.test_configparser import SortedDict


# #def has_duplicates(word: str) -> bool:
#     letters = {}
#
#     for letter in word:
#         if letter in letters:
#             return True
#
#         letters[letter] = True

def has_duplicates(word: str) -> bool:
    return len(word) != len(set(word))

with open("words.txt", "r") as file:
    words = file.read().splitlines()
    longest = 0
    longest_word = ""

    for word in words:
        if len(word) < longest:
            continue

        if has_duplicates(word):
            continue

        if len(word) > longest:
            longest = len(word)
            longest_word = word
    print(longest_word, longest)

with open("words.txt", "r") as file:
    words = file.read().splitlines()
    words = [word for word in words if len(word) == len(set(word))]
    word_lengths = {len(word): word for word in words}
    print(word_lengths[max(word_lengths.keys())])

#3rd option
#first get the longest words
#find one without duplicates in the longest
#if not


# inverted dicts

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

points = {"Anderlecht" : 33, "Club Brugge" : 41, "Genk": 42, "Antwerp": 32, "Union": 33}
rakings = SortedDict(invert_dict(points))
print(rakings)



def mean(lst1, lst2):
    index = ((len(lst1) + len(lst2)) // 2 ) // 2
    print((len(lst1) + len(lst2)) // 2)
    print(index)
    if (len(lst1) + len(lst2)) % 2 != 0:
        if lst1[index] < lst2[index]:
            return lst2[index]
        else:
            return lst1[index]
    else:
        if lst1[index] < lst2[index]:
            return (lst1[index] + (lst2[index] + 1) ) / 2
        else:
            return (lst1[index] + lst2[index]) / 2

lst1 = [1,3,5]
lst2 = [2,4,6,10]
#1 2 3 4 5 6 10

print(mean(lst1, lst2))
