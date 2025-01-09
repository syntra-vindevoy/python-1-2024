"""What is the longest word you can think of where each letter appears only once?
Let’s see if we can find one longer than unpredictably.

Write a function named has_duplicates that takes a sequence –
like a list or string – as a parameter and returns True if there is any element that appears in the sequence more than once.
"""


def has_duplicates(word):
    d = {}
    for letter in word:
        d [letter] = d.get(letter, 0) + 1
        if d[letter] > 1: return True

print(has_duplicates("hallo"))

with open ("words.txt", "r") as f:
    words = f.read().splitlines()
    words = [word for word in words if len(word) == len(set(word))]
    word_lenghts = {len(word): word for word in words}
print(sorted(word_lenghts, reverse=True)[0])
print (word_lenghts[max(word_lenghts.keys())])

def longest_word():
    with open ("words.txt", "r") as f:
        words = f.read().splitlines()
        words2 = {}
        for word in words:
            words2[word] = len(word)
        print (words2)
longest_word()
