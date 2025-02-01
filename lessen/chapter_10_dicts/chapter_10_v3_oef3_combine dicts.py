"""
Suppose you run value_counts with two different words and save the results in two dictionaries.


[ ]
counter1 = value_counts('brontosaurus')
counter2 = value_counts('apatosaurus')
Each dictionary maps from a set of letters to the number of times they appear. 
Write a function called add_counters that takes two dictionaries like this and returns a new dictionary that contains all of the letters and the total number of times they appear in either word.

There are many ways to solve this problem. 
Once you have a working solution, 
consider asking a virtual assistant for different solutions.
"""


def value_counts(word: str) -> dict[str, int]:
    counter = dict()
    for char in word:
        counter[char] = counter.get(char, 0) + 1
    return counter


counter1 = value_counts("brontosaurus")
counter2 = value_counts("apatosaurus")


def add_counters(counter_1, counter_2):
    counter = counter_1
    for char in counter_2:
        counter[char] = counter.get(char, 0) + counter_2[char]
    return counter


result = add_counters(counter1, counter2)

pass
