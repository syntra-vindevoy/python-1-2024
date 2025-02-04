def find_combination():
    with open("words.txt", "r") as f:
        words = f.read().splitlines()

    alphabet = list(string.ascii_lowercase)
    combinations = []

    for _ in range(5):
        count = {}
        for letter in alphabet:
            for word in words:
                if letter in word:
                    count[letter] = count.get(letter, 0) + 1

        lowest = min((count.keys()), key=count.get)

        alphabet.remove(lowest)
        combinations.append(lowest)

        words = [word for word in words if lowest not in word]

    return combinations, len(words)


import string
from time import perf_counter


def find_combination_list():
    with open("words.txt", "r") as f:
        words = {}
        for word in f.read().splitlines():
            # set to break down word in unique letters, sorted to have the same order every time, join to reform string
            new_word = "".join(sorted(set(word)))
            # shortens the words list and counts the amount of same combinations
            words[new_word] = words.get(new_word, 0) + 1

    alphabet = list(string.ascii_lowercase)
    combinations = []

    for _ in range(5):
        letter_count = 10000000
        for letter in alphabet:
            value_temp = 0

            for word, value in words.items():
                if letter in word:
                    value_temp += value

            if value_temp < letter_count:
                letter_count = value_temp
                temp_letter = letter

        temp_dict = words.copy()
        for word, value in temp_dict.items():
            if temp_letter in word:
                del words[word]

        # instead of the above, following dict comprehansion is slighly slower:
        # words = {key: value for key, value in words.items() if temp_letter not in key}

        combinations.append(temp_letter)
        alphabet.remove(temp_letter)

    return combinations, sum(words.values())


if __name__ == "__main__":
    start = perf_counter()
    combination, n = find_combination()
    stop = perf_counter()
    print(f" {n} results found without combination {combination} in {stop - start} seconds")
    start = perf_counter()
    combination, n = find_combination_list()
    stop = perf_counter()
    print(f" {n} results found without combination {combination} in {stop - start} seconds")
