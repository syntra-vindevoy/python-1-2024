"""
Exercise 9
Write a function that reads the file words.txt and builds a list with one element per word.
 Write two versions of this function, one using the append method and the other using the idiom t = t + [x].
 Which one takes longer to run? Why?

Elapsed time: 0.01 seconds
Elapsed time: 8.34 seconds
"""
import time


def read_words() -> [str]:
    words = []
    with open("words.txt", encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            words.append(word)
        return words


start_time = time.perf_counter()
assert len(read_words()) == 113783
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")


def read_words_lc() -> [str]:
    words = []
    with open("words.txt", encoding='utf-8') as file:
        return [word.strip() for word in file]


start_time = time.perf_counter()
assert len(read_words_lc()) == 113783
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")


def read_words2() -> [str]:
    words = []
    for line in open('words.txt', encoding='utf-8'):
        word = line.strip()
        words = words + [word]
    return words


start_time = time.perf_counter()
assert len(read_words2()) == 113783
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
