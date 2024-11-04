"""
10.11.3. Exercise
What is the longest word you can think of where each letter appears only once?
 Let’s see if we can find one longer than unpredictably.

Write a function named has_duplicates that takes a sequence – like a list or string – as a parameter and returns
True if there is any element that appears in the sequence more than once.
"""

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


assert find_repeats({'a': 1, 'b': 2, 'f': 5, 'c': 3, 'd': 1}) == ['b', 'f', 'c']

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


assert value_counts('brontosaurus') == {'a': 1, 'b': 1, 'n': 1, 'o': 2, 'r': 2, 's': 2, 't': 1, 'u': 2}


def add_counters(counter1, counter2):
    result = {}
    for key in counter1:
        if key in counter2:
            result[key] = counter1[key] + counter2[key]
        else:
            result[key] = counter1[key]
    return result


assert (add_counters(value_counts('brontosaurus'), value_counts('apatosaurus')) ==
        {'a': 4, 'b': 1, 'n': 1, 'o': 3, 'r': 3, 's': 4, 't': 2, 'u': 4})

"""
10.11.6. Exercise
A word is “interlocking” if we can split it into two words by taking alternating letters. For example, “schooled” is an
 interlocking word because it can be split into “shoe” and “cold”.

To select alternating letters from a string, you can use a slice operator with three components that indicate where
 to start, where to stop, and the “step size” between the letters.

In the following slice, the first component is 0, so we start with the first letter. The second component is None, 
which means we should go all the way to the end of the string. And the third component is 2, 
so there are two steps between the letters we select.

word = 'schooled'
first = word[0:None:2]
first
'shoe'
Instead of providing None as the second component, we can get the same effect by leaving it out altogether. 
For example, the following slice selects alternating letters, starting with the second letter.

second = word[1::2]
second
'cold'
Write a function called is_interlocking that takes a word as an argument 
and returns True if it can be split into two interlocking words.
"""
