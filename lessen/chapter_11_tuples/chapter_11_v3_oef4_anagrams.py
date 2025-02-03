from icecream import ic
import os


script_dir = os.path.dirname(__file__)
file_name = "words.txt"
file_path = os.path.join(script_dir, file_name)

with open(file_path, "r") as f:
    word_list = f.read().split()

word_dict = {}
for word in word_list:
    sorted_word = tuple(sorted(word))
    pass
    if sorted_word not in word_dict:
        word_dict[sorted_word] = list()
    word_dict[sorted_word].append(word)

# word_dict = {word: "".join(sorted(word)) for word in word_list}


def anagram_length(t):
    return len(t[1])


def word_length(w):
    return len(w[0])


# woord met meeste anagrammen
print("anagram met meeste woorden")
longest_anagram_count = 0
for key, value in word_dict.items():
    if len(value) > longest_anagram_count:
        longest_anagram_count = len(value)

sorted_items = sorted(word_dict.items(), key=anagram_length, reverse=True)

filtered_items = [
    item for item in sorted_items if len(item[1]) == longest_anagram_count
]
for item in filtered_items:
    ic(item[1])

# anagram met langste lengte
print("anagram met langste lengte:")
filtered_items = [item for item in sorted_items if len(item[1]) >= 2]
longest_word_length = 0
for item in filtered_items:
    if len(item[0]) > longest_word_length:
        longest_word_length = len(item[0])
result = [item for item in filtered_items if len(item[0]) == longest_word_length]

ic(result)

"""
def word_to_counter_dict(word):
    counter_dict = {}
    for char in word:
        if char in counter_dict:
            counter_dict[char] += 1
        else:
            counter_dict[char] = 1
    return counter_dict


def inverted_dict(d):
    temp_dict = dict()
    for key, value in d.items():
        if value not in temp_dict:
            temp_dict[value] = list()
        temp_dict[value].append(key)
    return temp_dict

"""
