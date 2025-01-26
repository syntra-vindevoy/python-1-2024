import string
from time import perf_counter

def find_combination():
    with open("words.txt", "r") as f:
        words ={}
        for word in f.read().splitlines():
            new_word = "".join(sorted(set(word)))
            words[new_word] = words.get(new_word, 0) + 1

    alphabet = list (string.ascii_lowercase)

    print (sum(words.values()))
    combinations = []

    for _ in range (5):
        value_letter = 10000000
        for letter in alphabet:
            value_temp = 0

            for word, value in words.items():

                if letter in word:
                    value_temp += value

            if value_temp < value_letter:
                value_letter = value_temp
                temp_letter = letter
        temp_dict = words.copy()
        for word, value in temp_dict.items():
            if temp_letter in word:
                del words[word]

        combinations.append(temp_letter)
        alphabet.remove(temp_letter)

    return combinations, sum(words.values())

if __name__ == "__main__":
    start = perf_counter()
    combination, n = find_combination()
    stop = perf_counter()
    print (f" {n} results found without combination {combination} in {stop - start} seconds")
