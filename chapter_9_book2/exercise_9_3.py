import string
from time import perf_counter

def find_combination():
    with open("words.txt", "r") as f:
        words = f.read().splitlines()
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

        words = [word for word in words if temp_letter not in word]

        combinations.append(temp_letter)
        alphabet.remove(temp_letter)

    return combinations, len(words)

if __name__ == "__main__":
    start = perf_counter()
    combination, n = find_combination()
    stop = perf_counter()
    print (f" {n} results found without combination {combination} in {stop - start} seconds")
