from sortedcontainers import SortedDict


def has_duplicates(word: str) -> bool:
    letters = {}

    for letter in word:
        if letter in letters:
            return True

        letters[letter] = True


def has_duplicates2(word: str) -> bool:
    return len(word) > len(set(word))


with open("words.txt", "r") as file:
    words = file.read().splitlines()
    longest = 0
    longest_word = ""

    for word in words:
        if len(word) < longest:
            continue

        if has_duplicates(word):
            continue

        if len(word) > longest:
            longest = len(word)
            longest_word = word

    print(longest_word, longest)

with open("words.txt", "r") as file:
    words = file.read().splitlines()

    words = [word for word in words if len(word) == len(set(word))]
    word_lengths = {len(word): word for word in words}

    print(word_lengths[max(word_lengths.keys())])


# 3rd option
# first get the longest words
# find one without duplicates in the longest
# if not found, descend


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


points = {"Anderlecht": 33, "Club Brugge": 41, "Genk": 42, "Antwerp": 32, "Union": 33}
rankings = SortedDict(invert_dict(points))

print(rankings)

## Ex: write the rankings WITHOUT inverted dict
