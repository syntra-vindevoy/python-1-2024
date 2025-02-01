"""
Write a function called most_frequent_letters that takes a string and prints the letters in decreasing order of frequency.

To get the items in decreasing order, you can use reversed along with sorted or you can pass reverse=True as a keyword parameter to sorted.
"""

from icecream import ic


def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter


def second_element(t):
    return t[1]


print(value_counts("bananas"))
items = value_counts("bananas").items()
sorted_items = sorted(items, key=second_element)

ic(sorted_items)
