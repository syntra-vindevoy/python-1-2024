"""What is the longest word you can think of where each letter appears only once?
Let’s see if we can find one longer than unpredictably.

Write a function named has_duplicates that takes a sequence –
like a list or string – as a parameter and returns True if there is any element that appears in the sequence more than once.
"""

def has_duplicates(word_list):
    d = {}
    for word in word_list:
        d [word] = d.get(word, 0) + 1
        if d[word] > 1: return True

print(has_duplicates(["hallo", "hal", "aj", "jh", "ha"]))
