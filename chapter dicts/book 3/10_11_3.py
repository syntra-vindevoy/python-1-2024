"""What is the longest word you can think of where each letter appears only once?
Let’s see if we can find one longer than unpredictably.

Write a function named has_duplicates that takes a sequence –
like a list or string – as a parameter and returns True if there is any element that appears in the sequence more than once.
"""
from sortedcontainers import SortedDict

def has_duplicates(word):
    d = {}
    for letter in word:
        d [letter] = d.get(letter, 0) + 1
        if d[letter] > 1: return True

print(has_duplicates("hallo"))

with open ("../words.txt", "r") as f:
    words = f.read().splitlines()
    words = [word for word in words if len(word) == len(set(word))]
    word_lenghts = {len(word): word for word in words}
print(sorted(word_lenghts, reverse=True)[0])
print (word_lenghts[max(word_lenghts.keys())])

def longest_word():
    with open ("../words.txt", "r") as f:
        words = f.read().splitlines()
        words2 = {}
        for word in words:
            words2[word] = len(word)

    words_sorted = sorted(words2.items(), key=lambda x: x[1], reverse=True)

    for word in words_sorted:
        if not has_duplicates(word[0]): return word

print (longest_word())

"""de sorted()-functie sorteert de lijst van tuples. 
        De argumenten binnen sorted() bepalen hoe de sortering wordt uitgevoerd.

    key=lambda x: x[0]:
        De key-parameter bepaalt op welke eigenschap de sortering gebaseerd is.
        lambda x: x[0] betekent: neem het eerste element (x[0]) van elk tuple als de sorteerbasis.
        In dit geval verwijst x[0] naar de sleutel in elk tuple
"""

