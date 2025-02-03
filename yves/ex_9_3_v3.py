import itertools
import string
import sys
from datetime import datetime

# 96425
# qjxzw
# print(words_without(list("qjxzw")))


with open("words.txt", "r") as input_file:
    all_words = input_file.readlines()


# def avoids(forbidden, word):
#     for letter in forbidden:
#         if letter in word:
#             return False
#
#     return True
#
#
# def words_without(forbidden):
#     count = 0
#
#     for word in all_words:
#         if avoids(forbidden, word):
#             count += 1
#
#     return count

def words_with(words, contains):
    return sum([any([letter in word for letter in contains]) for word in words])


def run():
    start = datetime.now()

    # print(0, len(all_words))

    words = [set(word.strip()) for word in all_words]
    # print(1, words)
    letter_count = {letter: len([word for word in words if letter in word]) for letter in string.ascii_lowercase}
    # print(2, letter_count)
    letter_count = sorted(letter_count.items(), key=lambda x: x[1])
    # print(3, letter_count)
    least_five = letter_count[:5]
    # print(4, least_five)
    sum_least_five = sum([lf[1] for lf in least_five])
    # print(5, sum_least_five)
    least_five_letters = [lf[0] for lf in least_five]
    # print(6, least_five_letters)
    words_with_least = words_with(words, least_five_letters)
    # print(7, words_with_least)
    to_check = [letter[0] for letter in letter_count if letter[1] < words_with_least]
    # print(8, to_check)

    words_to_check = [word for letter in to_check for word in words if letter in word]
    # print(9, words_to_check)
    # print(10, len(words_to_check))

    combinations = list(itertools.combinations(to_check, 5))
    # print(11, len(combinations))
    # print(12, combinations)

    checks = {c: words_with(words_to_check, c) for c in combinations}
    # print(13, checks)

    checks_sorted = sorted(checks.items(), key=lambda x: x[1])
    # print(14, checks_sorted)

    best_check = checks_sorted[0]
    # print(15, best_check)

    print(f"Best combination: {best_check[0]}: {best_check[1]} times")

    end = datetime.now()
    print(end - start)


if __name__ == "__main__":
    run()
