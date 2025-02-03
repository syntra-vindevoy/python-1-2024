import string
from datetime import datetime
from itertools import combinations

from tqdm import tqdm

# def five_chars_1():
#     combinations = []
#
#     for l_1 in string.ascii_lowercase[:22]:
#         for l_2 in string.ascii_lowercase[1:23]:
#             for l_3 in string.ascii_lowercase[2:24]:
#                 for l_4 in string.ascii_lowercase[3:25]:
#                     for l_5 in string.ascii_lowercase[4:26]:
#                         combinations.append([l_1, l_2, l_3, l_4, l_5])
#
#     print("Number of combinations:", len(combinations)) # 5153632
#
#     with open("words.txt", "r") as file:
#         words = file.read().splitlines()
#
#     print("Number of words:", len(words))  # 113809
#
#     min_found = len(words)
#     combo = []
#
#     progress_bar = tqdm(total=(len(combinations) * len(words)), bar_format="{l_bar}{bar} | {n:,}/{total:,} Elapsed: {elapsed} | Remaining: {remaining}")
#
#     for combination in combinations:
#         count_words = 0
#
#         for word in words:
#             progress_bar.update(1)
#             found = False
#
#             for letter in combination:
#                 if letter in word:
#                     found = True
#
#             if not found:
#                 count_words += 1
#
#         if count_words < min_found:
#             min_found = count_words
#             combo = combination
#
#     print(combo, min_found)


def five_chars_2():
    start = datetime.now()

    with open("words.txt", "r") as file:
        words = file.read().splitlines()

    orig_length = len(words)

    usage = {c: sum([c in w for w in words]) for c in string.ascii_lowercase}
    print("How many words contain the letter:", usage)

    candidate = sorted(usage.items(), key=lambda x: x[1])[:5]
    print("Candidate:", candidate)

    boundary = sum([s[1] for s in candidate])
    print("The five lowest summed:", boundary)

    usage = [u for u in usage if usage[u] < boundary]
    print("We only need to check:", usage)

    usage_set = set(usage)
    words = [word for word in words if set(usage).intersection(word)]
    # words = [word for word in words if usage_set & set(word)]  # Use set intersection
    # words = [word for word in words if any(char in usage_set for char in word)]
    print("Number of words with usage:", len(words))

    combos = list(combinations(usage, 5))
    print("Number of combinations to review:", len(combos))

    combo_usage = {combo: sum(1 for word in words if any(c in word for c in combo)) for combo in combos}
    print(combo_usage)

    the_combo = sorted(combo_usage, key=lambda x: combo_usage[x])[0]
    print("Least used:", the_combo, "with usage:", combo_usage[the_combo])
    print("Number of words without our combo:", orig_length - combo_usage[the_combo])

    end = datetime.now()
    print("I got my answer in", end - start, "seconds")





if __name__ == "__main__":
    five_chars_2()

