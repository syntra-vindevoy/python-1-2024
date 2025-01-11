import string
from time import perf_counter

def find_combination():
    with open("words.txt", "r") as f:
        words = f.read().splitlines()

    alphabet = list (string.ascii_lowercase)
    combinations = []

    for _ in range (5):
        count = {}
        for letter in alphabet:
            for word in words:
                if letter in word:
                    count[letter] = count.get(letter, 0) + 1

        lowest = min((count.keys()), key = count.get)

        alphabet.remove(lowest)
        combinations.append(lowest)

        words = [word for word in words if lowest not in word]


    return combinations, len(words)

if __name__ == "__main__":
    start = perf_counter()
    combination, n = find_combination()
    stop = perf_counter()
    print (f" {n} results found without combination {combination} in {stop - start} seconds")

#origineel zonder dict = 0.38sec
#met dict = 0.5sec
#met set.words e.d. ook trager