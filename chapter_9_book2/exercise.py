import string
from itertools import combinations
from time import perf_counter


def uses_none(word, forbidden):
    for letter in forbidden:
        if letter in word: return False
    return True

def find_combination():
    with open("words.txt", "r") as f:
        words = f.read().split("\n")
    alphabet = list (string.ascii_lowercase)
    combinations = []

    for _ in range (5):
        value = 10000000
        for letter in alphabet:
            value_temp = 0
            for word in words:
                if letter in word:
                    value_temp += 1

            if value_temp < value:
                value = value_temp
                temp_letter = letter

        combinations.append(temp_letter)
        alphabet.remove(temp_letter)
    n = 0
    for word in words:
        if uses_none(word, combinations): n += 1

    return (combinations, n)


if __name__ == "__main__":
    start = perf_counter()
    combination, n = find_combination()
    stop = perf_counter()
    print (f"{n} results found with combination {combination} in {stop - start} seconds")









