from collections import defaultdict
import collections
"""
10.11.3. Exercise
What is the longest word you can think of where each letter appears only once?
 Let’s see if we can find one longer than unpredictably.
Write a function named has_duplicates that takes a sequence – like a list or string – as a parameter and returns
True if there is any element that appears in the sequence more than once.
"""
def has_duplicates_len(words: list)->bool:
   return len(set(words)) < len(words)

def longest_word(word_list):
    longest=0
    lw = ''
    for word in word_list:
        if len(word) < longest:
            continue
        if has_duplicates_len(word):
            continue
        if len(word) > len(lw):
            longest=len(word)
            lw = word
    print(lw,longest)

with open('words.txt') as file:
    word_list = file.read().splitlines()
    longest_word(word_list)


def longest_word_n():
    with open('words.txt') as file:
        wls = file.read().splitlines()
        words=[word for word in wls if len(word) == len(set(word))]
        word_lengths ={len(word):word for word in words}

        print(word_lengths[max(word_lengths.keys())])

assert has_duplicates_len(['a', 'b', 'c', 'a']) == True

longest_word_n()

"""
10.11.4. Exercise
Write function called find_repeats that takes a dictionary that maps from each key to a counter,
like the result from value_counts. It should loop through the dictionary and
return a list of keys that have counts greater than 1. You can use the following outline to get started.
"""


def find_repeats(counter):
    list_greater = []
    for key, value in counter.items():
        if value > 1:
            list_greater.append(key)
    return list_greater


def find_repeats2(counter:dict):
    return [x for x,y in counter.items() if y> 1]


assert find_repeats({'a': 1, 'b': 2, 'f': 5, 'c': 3, 'd': 1}) == ['b', 'f', 'c']
assert find_repeats2({'a': 1, 'b': 2, 'f': 5, 'c': 3, 'd': 1}) == ['b', 'f', 'c']
"""
10.11.5. Exercise
Suppose you run value_counts with two different words and save the results in two dictionaries.

counter1 = value_counts('brontosaurus')
counter2 = value_counts('apatosaurus')
Each dictionary maps from a set of letters to the number of times they appear. Write a function called add_counters
 that takes two dictionaries like this and returns a new dictionary that contains all of the letters and
  the total number of times they appear in either word.

There are many ways to solve this problem. Once you have a working solution, consider asking a virtual assistant
 for different solutions.
"""

def value_counts(word):
    counter = {}
    for letter in word:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter

def value_counts2(word):
    def _increment_counter(counter, character):
        counter[character] += 1

    character_counter = defaultdict(int)
    for char in word:
        _increment_counter(character_counter, char)
    return dict(character_counter)

def value_counts3(word):
   return collections.Counter(word)

assert value_counts('brontosaurus') == {'a': 1, 'b': 1, 'n': 1, 'o': 2, 'r': 2, 's': 2, 't': 1, 'u': 2}
assert value_counts2('brontosaurus') == {'a': 1, 'b': 1, 'n': 1, 'o': 2, 'r': 2, 's': 2, 't': 1, 'u': 2}
assert value_counts3('brontosaurus') == {'a': 1, 'b': 1, 'n': 1, 'o': 2, 'r': 2, 's': 2, 't': 1, 'u': 2}
assert value_counts3('apatosaurus') == {'a': 3, 's': 2, 'u': 2, 'p': 1, 't': 1, 'o': 1, 'r': 1}
assert value_counts2('apatosaurus') == {'a': 3, 's': 2, 'u': 2, 'p': 1, 't': 1, 'o': 1, 'r': 1}
assert value_counts('apatosaurus') == {'a': 3, 's': 2, 'u': 2, 'p': 1, 't': 1, 'o': 1, 'r': 1}

def add_counters(counter1, counter2):
    result = {}
    all_keys = set(counter1.keys()).union(counter2.keys())
    for key in all_keys:
        result[key] = counter1.get(key, 0) + counter2.get(key, 0)
    return result

def add_counters_faster(counter1, counter2):
    return collections.Counter(counter1+counter2)

assert (add_counters(value_counts('brontosaurus'), value_counts('apatosaurus')) ==
        {'a': 4, 'b': 1, 'n': 1, 'o': 3, 'p': 1, 'r': 3, 's': 4, 't': 2, 'u': 4})

assert (add_counters(value_counts3('brontosaurus'), value_counts3('apatosaurus')) == {'a': 4, 'b': 1, 'n': 1, 'o': 3, 'p': 1, 'r': 3, 's': 4, 't': 2, 'u': 4})

assert (dict(sorted(add_counters_faster('brontosaurus', 'apatosaurus').items())) ==
        {'a': 4, 'b': 1, 'n': 1, 'o': 3, 'p': 1, 'r': 3, 's': 4, 't': 2, 'u': 4})
"""
10.11.6. Exercise

Write a function called is_interlocking that takes a word as an argument 
and returns True if it can be split into two interlocking words.
"""
def is_interlocking(word, word_list):
    """
    Determines if a word can be split into two interlocking words.

    Args:
    - word (str): The input word to check.
    - word_list (set): A set of valid words for interlocking comparison.

    Returns:
    - bool: True if the word can be split into two interlocking words, False otherwise.
    """
    # Split the word into characters at even and odd indices
    word1 = word[::2]  # Characters at even indices
    word2 = word[1::2]  # Characters at odd indices

    # Check if both generated words exist in the word_list
    return word1 in word_list and word2 in word_list
from sortedcontainers import SortedDict

def interlocking_set():
    with open ("words.txt", "r") as f:
        words = f.read().splitlines()
        words =set(words)
    interlocking = SortedDict({word: (word[0::2], word[1::2]) for word in words if word[0::2] in words and word[1::2] in words})
    return interlocking

assert is_interlocking('brontosaurus', {'brontosaurus', 'apatosaurus', 'triceratops', 'botsuu', 'rnoars'}) == True

print(interlocking_set())
