import string
import operator
import functools
import itertools

with open('words.txt', 'r') as f:
    words = f.readlines()

alphabet = string.ascii_lowercase
sets = {letter: {ix for ix, word in enumerate(words) if letter in word} for letter in alphabet}
sorted_alphabet = sorted(alphabet, key=lambda t: len(sets[t]))


def count_words(combination):
    all_sets = [sets[combination] for combination in combination]
    union = functools.reduce(operator.or_, all_sets)

    return len(union)


candidate_count = count_words(sorted_alphabet[:5])
rest_alphabet = [letter for letter in sorted_alphabet if len(sets[letter]) <= candidate_count]
minimum, winner = len(words), ''

for combination in itertools.combinations(rest_alphabet, 5):
    count = count_words(combination)

    if count <= minimum:
        minimum, winner = count, combination

print(minimum, winner)
