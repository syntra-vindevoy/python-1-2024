"""1. Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of
words that are anagrams.
Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
Hint: you might want to build a dictionary that maps from a collection of letters to a list
of words that can be spelled with those letters. The question is, how can you represent the
collection of letters in a way that can be used as a key?
2. Modify the previous program so that it prints the longest list of anagrams first, followed by
the second longest, and so on.
3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on
the board, to form an eight-letter word. What collection of 8 letters forms the most possible
bingos?"""
from pathlib import Path

words_dir = Path("C:/Syntra")
file_name = "words.txt"
file = words_dir / file_name

# def anagrams(file):
#     with open (file, "r") as f:
#         words = f.read().splitlines()
#         words_sorted = {}
#     for word in words:
#         words_sorted["".join (sorted(word))] = word
#     return words_sorted
# print(anagrams(file))

def anagrams(file):
    with open(file, "r") as f:
        words_sorted = {}
        for word in f.read().splitlines():
            key = "".join(sorted(word))
            words_sorted.setdefault(key, []).append(word)

    #makes a dict with only the true anagrams
    anagrams_only = {key: value for key, value in words_sorted.items() if len(value) >= 2}

    #sorts the dict by number of values, did not work without the itteration
    anagrams_sorted = {key: value for key, value in
                       sorted(anagrams_only.items(), key=lambda item: len(item[1]), reverse=True)}

    eight_letter_anagrams = {key: value for key, value in anagrams_only.items() if len(key) == 8}


    return anagrams_sorted.values()

print (anagrams(file))
"""Exercise 12.3. Two words form a “metathesis pair” if you can transform one into the other by
swapping two letters; for example, “converse” and “conserve”. Write a program that finds all of
the metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t test all possible
swaps"""

anagrams = anagrams(file)
#print (len(anagrams))

def metathesis_pairs():
    for words in anagrams:
        single_lenght = len(words[0])
        number = len(words)
        connected_word = "".join(words)
        count = 0
        pair = False

        for i in range(single_lenght):
            if connected_word[i] == connected_word[i + single_lenght]: #klopt nog niet voor meer dan 2 woorden
                count += 1
        if count == 2:
            pair = True
        print (single_lenght, connected_word)
metathesis_pairs()



