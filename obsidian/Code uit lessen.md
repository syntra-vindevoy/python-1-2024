# General

demo_args.py args kwargs
```python
def mean(*args):
    return sum(args) / len(args)


t = [1, 2, 3, 4, 5]
print(mean(*t))


def toto(**kwargs):
    for kw in kwargs:
        print(f"{kw}: {kwargs[kw]}")


print(toto(a=1, b=2, c=3))

d = {"a": 1, "b": 2, "c": 3}
print(toto(**d))


def homepage(request, *args, **kwargs):
    pass
```

demo_digest.py
```python
import hashlib

def md5_hash(string):
    """
    Generate the MD5 hash of a given string.

    :param string: Input string to be hashed
    :return: MD5 hash of the input string
    """
    # Create MD5 hash object
    md5 = hashlib.md5()

    # Encode the string and generate the hash
    md5.update(string.encode('utf-8'))

    # Return the hexadecimal representation of the hash
    return md5.hexdigest()


def md5_digest(filename):
    data = open(filename, 'rb').read()
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    digest = md5_hash.hexdigest()
    return digest

#print(md5_digest("words.txt"))
#print(md5_digest("words2.txt"))

print(md5_hash("aa"))
```

demo_files.py
```python
from pathlib import Path

current_path = Path(__file__).parent
root_path = current_path.parent

my_python_files = root_path.rglob("**/*.py")

print(list(my_python_files))
```

demo_generator.py
```python

import timeit
import tracemalloc
from pathlib import Path


def generate_large_file(filename, num_lines):
    from lorem import sentence

    with open(filename, "w") as f:
        for _ in range(num_lines):
            f.write(sentence() + "\n")


# Function to measure memory usage
def measure(func, times=1, *args):
    method = args[0]

    tracemalloc.start()
    execution_time = timeit.timeit(lambda: func(method=method), setup="from __main__ import read", number=times)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    current_mb = current / 1024 / 1024
    peak_mb = peak / 1024 / 1024

    return method, execution_time, current_mb, peak_mb


def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()

        return lines


def read_yield(path):
    with open(path, "r") as f:
        for line in f:
            yield line


def read(method: int):
    path = Path(__file__).parent.joinpath("lorem.txt").resolve()

    if method == 1:
        lines = read_file(path)
    else:
        lines = read_yield(path)

    total_lines = 0
    vowel_lines = 0

    for line in lines:
        total_lines += 1

        if line.strip()[:1].upper() in "AEIOUY":
            vowel_lines += 1

    print(
        "Method:",
        "NORMAL" if method == 1 else "YIELD ",
        "- File",
        path,
        "has",
        vowel_lines,
        "lines starting with a vowel on a total of",
        total_lines,
        "lines:",
        vowel_lines * 100 // total_lines,
        "%",
        )


def main():
    times = 5

    method_1, execution_time_1, current_mb_1, peak_mb_1 = measure(read, times, 1)
    method_2, execution_time_2, current_mb_2, peak_mb_2 = measure(read, times, 2)

    print("\nNORMAL READ" if method_1 == 1 else "YIELD READ")
    print(f"  - Average execution time over {times} runs: {execution_time_1 / times:.5f} seconds")
    print(f"  - Current memory usage: {current_mb_1:.5f} MB")
    print(f"  - Peak memory usage: {peak_mb_1:.5f} MB\n")

    print("\nNORMAL READ" if method_2 == 1 else "YIELD READ")
    print(f"  - Average execution time over {times} runs: {execution_time_2 / times:.5f} seconds")
    print(f"  - Current memory usage: {current_mb_2:.5f} MB")
    print(f"  - Peak memory usage: {peak_mb_2:.5f} MB\n")



if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     number_of_lines = 2 * 1000 * 1000
#
#     output_file = Path(__file__).parent.joinpath("lorem.txt").resolve()
#     generate_large_file(output_file, number_of_lines)
#     print(f"File '{output_file}' with {number_of_lines} lines was successfully created.")
#

```

demo_notebook.py
```python
#%%
import os
from pathlib import Path

import pandas as pd
import numpy as np

#%%
current_path = os.getcwd()
print(current_path)
df = pd.read_csv(os.path.join(current_path, "words.txt"))

#%%
print(df.info())
```

demo_version.py
```python
def version_part(s: str):
    if s.isnumeric():
        return int(s), s
    else:
        return 0, s

def version_is_newer(old_version, new_version):
    old_version = str(old_version).split(".")
    old_version = tuple(old_version)

    old_version = [version_part(v) for v in old_version]
    old_version = tuple(old_version)
    #print(old_version)

    new_version = str(new_version).split(".")
    new_version = tuple(new_version)

    new_version = [version_part(v) for v in new_version]
    new_version = tuple(new_version)
    #print(new_version)

    return new_version > old_version


import re

import re


import re


import re


def version_check(old_version, new_version):
    # Define the semantic ordering for known pre-release keywords
    pre_release_order = {
        "snapshot": 3,  # Higher number means newer
        "alpha": 2,
        "beta": 4,
        "milestone": 1,
        "rc": 5,  # Release Candidate
        "final": 6  # Final release is the newest
    }

    def normalize_version(version):
        # Ensure the input is a string
        version = str(version)
        # Use regex to extract parts (numbers or non-numeric segments)
        parts = re.findall(r'(\d+|[^\d.]+)', version)
        normalized = []
        for part in parts:
            if part.isdigit():
                # Convert numeric parts to integers
                normalized.append(int(part))
            else:
                normalized.append(
                    # Use semantic ordering for known pre-release tags
                    pre_release_order.get(part.lower(), part.lower())
                )
        return tuple(normalized)

    # Normalize both versions for comparison
    old_parts = normalize_version(old_version)
    new_parts = normalize_version(new_version)

    # Compare the normalized tuples lexicographically
    return new_parts > old_parts

if __name__ == "__main__":
    assert version_check(1, 2)
    assert version_check(1.0, 2.0)

    assert version_check("1.0", "2.0")
    assert version_check("3.0", "11.0")
    assert version_check("3.0", "11.0.0")

    assert version_check("1.0.0", "1.0.1")
    assert version_check("1.0.2", "1.0.10")

    assert version_check("1.a", "1.b")
    assert version_check("1.b", "2.a")

    assert version_check("1.0", "1.0_alpha")
    assert version_check("1.0.snapshot", "1.0.milestone")
```

demo_yaml.py
```python
import yaml


with open ("test.yaml", "r") as yaml_file:
    content = yaml.safe_load(yaml_file)

print(content)

for c in content["cities_lived"]:
    print(c)
```

# Lists

# Dicts

demo_dict.py
```python
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
```


# Tuple

demo_tuple.py
```python
x = (1, 2)

y = 1, 2

print(type(x))
print(type(y))


a = 1
b = 2

a, b = b, a

c = (a, b)

y = ("yves",)
print(y)

print(y[0])
print(len(y))

print(sorted(tuple("yves")))


# t = (1, 2, "y", [1, 2, 3])
# print(sorted(t))

a, b = 1, 2
print(a)


d, e, _, f = 1, 2, 3, 4

print(_)
```


ex_10_01.py
```python
def nested_sum(lists: list[int|float]) -> float:
    s = 0

    for lst in lists:
        for item in lst:
            s += item

    return s


def nested_sum2(lists: list[int|float]) -> float:
    return sum([sum(lst) for lst in lists])

if __name__ == '__main__':
    print(nested_sum2([[1, 2], [3, 4, 5], [6.0]]))
```

ex_10_02.py
```python
def cumsum(lst: list[int]) -> list[int]:
    nl = []
    s = 0

    for i in lst:
        s += i
        nl.append(s)

    return nl

def cumsum2(lst: list[int]) -> list[int]:
    return [sum(lst[0:i+1]) for i in range(len(lst))]


if __name__ == '__main__':
    print(cumsum2([1, 2, 3, 4]))
```

ex_10_03.py
```python
def middle(lst: list) -> list:
    return lst[1:-1]


if __name__ == '__main__':
    print(middle([1,2, 3, 4, 5]))
```

ex_10_04.py
```python
def chop(lst):
    del lst[0]
    del lst[-1]


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8]

    print(chop(lst))
    print(lst)
```

ex_10_05.py
```python
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True

def is_sorted2(lst):
    return all([lst[i] <= lst[i + 1] for i in range(len(lst) - 1)])



if __name__ == '__main__':
    print(is_sorted([1, 2, 3, 4]))
    print(is_sorted2([1, 2, 3, 0]))
```

ex_10_06.py
```python
import logging

logger = logging.getLogger(__name__)


def is_anagram(str1, str2):
    equal = sorted(str1.lower()) == sorted(str2.lower())
    logger.error(f"{str1} and {str2} are anagrams: {equal}")
    return equal


if __name__ == '__main__':
    print(is_anagram('yves', 'sevy'))
```

ex_10_07.py
```python
def has_duplicates(lst: list):
    copy_lst = lst.copy()
    sorted_lst = sorted(copy_lst)

    for i in range(len(sorted_lst) - 1):
        if sorted_lst[i] == sorted_lst[i + 1]:
            print(sorted_lst[i])
            return True

    return False
```

ex_10_08.py
```python
from random import random, randint

from ex_10_7 import has_duplicates

def get_birthdays(nbr: int):
    return [randint(1, 365) for _ in range(nbr)]

def test(nbr):
    same_birthdays = 0

    for i in range(nbr):
        birthdays = get_birthdays(23)
        # print(birthdays)
        if has_duplicates(birthdays):
            print(birthdays)
            same_birthdays += 1

    return same_birthdays, nbr


if __name__ == '__main__':
    s, n = test(10)

    print(s / n)
```

ex_10_09.py
```python
from random import random, randint

from ex_10_7 import has_duplicates

def get_birthdays(nbr: int):
    return [randint(1, 365) for _ in range(nbr)]

def test(nbr):
    same_birthdays = 0

    for i in range(nbr):
        birthdays = get_birthdays(23)
        # print(birthdays)
        if has_duplicates(birthdays):
            print(birthdays)
            same_birthdays += 1

    return same_birthdays, nbr


if __name__ == '__main__':
    s, n = test(10)

    print(s / n)
```


ex_10_10.py
```python
def bisect_search(sorted_list, item, step = 1):
    if len(sorted_list) == 1:
        return item == sorted_list[0], step

    middle_index = len(sorted_list) // 2
    middle_item = sorted_list[middle_index]

    if middle_item == item:
        return True, step

    if middle_item > item:
        return bisect_search(sorted_list[:middle_index], item, step + 1)
    else:
        return bisect_search(sorted_list[middle_index+1:], item, step + 1)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(bisect_search(lst, 1))
    print(bisect_search(lst,2))
    print(bisect_search(lst,3))
    print(bisect_search(lst,4))
    print(bisect_search(lst,5))
    print(bisect_search(lst,6))
    print(bisect_search(lst,7))
    print(bisect_search(lst,8))
    print(bisect_search(lst,9))
    print(bisect_search(lst,10))

    print(bisect_search(lst, 0))
    print(bisect_search(lst, 11))
```

ex_10_10_v2.py
```python
def bisect_search(sorted_list, item):
    step = 0

    while True:
        step += 1
        middle_index = len(sorted_list) // 2
        middle_item = sorted_list[middle_index]

        if middle_item == item:
            return True, step

        if middle_item > item:
            sorted_list = (sorted_list[:middle_index])
        else:
            sorted_list = sorted_list[middle_index+1:]

        if len(sorted_list) == 0:
            return False, step


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(bisect_search(lst, 1))
    print(bisect_search(lst,2))
    print(bisect_search(lst,3))
    print(bisect_search(lst,4))
    print(bisect_search(lst,5))
    print(bisect_search(lst,6))
    print(bisect_search(lst,7))
    print(bisect_search(lst,8))
    print(bisect_search(lst,9))
    print(bisect_search(lst,10))

    print(bisect_search(lst, 0))
    print(bisect_search(lst, 11))
```

ex_10_10_v3
```python
def bisect_search(sorted_list, item):
    step = 0
    marker_low = 0
    marker_high = len(lst) - 1

    while True:
        step += 1
        marker_middle = (marker_low + marker_high) // 2
        item_middle = sorted_list[marker_middle]

        if item_middle == item:
            return True, step

        if item_middle > item:
            marker_high = marker_middle - 1
        else:
            marker_low = marker_middle + 1

        if marker_low == marker_high:
            return sorted_list[marker_low] == item, step


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(bisect_search(lst, 1))
    print(bisect_search(lst,2))
    print(bisect_search(lst,3))
    print(bisect_search(lst,4))
    print(bisect_search(lst,5))
    print(bisect_search(lst,6))
    print(bisect_search(lst,7))
    print(bisect_search(lst,8))
    print(bisect_search(lst,9))
    print(bisect_search(lst,10))

    print(bisect_search(lst, 0))
    print(bisect_search(lst, 11))
```

ex_10_11.py
```python
with open("words.txt") as file:
    words = file.readlines()

    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if words[i].strip() == words[j].strip()[::-1]:
                print(words[i].strip(), words[j].strip())
```


ex_10_11_v2.py
```python
def has_reversed_pairs(words):
    repairs = []

    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if words[i] == words[j][::-1]:
                repairs.append(words[i])
                repairs.append(words[j])

    return repairs


with open("words.txt") as file:
    words = file.readlines()

    pairs = {}

    for word in words:
        word = word.strip()
        key = "".join(sorted(word))

        if key in pairs:
            pairs[key].append(word)
        else:
            pairs[key] = [word]

    for pair in pairs:
        if len(pair) > 1:
            repairs = has_reversed_pairs(pairs[pair])

            if len(repairs) > 1:
                print(repairs)
```

ex_10_12.py
```python
def interlock(str1, str2):
    zipped = zip(str1, str2, strict=False)

    interlocked = "".join(["".join(z) for z in zipped])

    if len(str1) != len(str2):
        if len(str1) > len(str2):
            interlocked += str1[len(str2):]
        else:
            interlocked += str2[len(str1):]


if __name__ == '__main__':
    interlock("abc", "defghi")
```

five_chars.py
```python
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
```

try_demo.py
```python
def toto(l):
    pass

f = None

try:
    f = open("words.txt", "r")
    lines = f.readlines()

    toto(lines)

except SyntaxError:
    print("Your code sucks")

except FileNotFoundError:
    print("Could not find file")

except Exception as err:
    print("Did not really expect this one", err)

finally:
    if f:
        if not f.closed:
            f.close()





def fac(n):
    if n < 0:
        raise ValueError(f"n must be non-negative, you entered {n}")

    if n < 2:
        return 1

    return n * fac(n-1)


i = input("Give a positive integer:")

try:
    print(fac(int(i)))
except ValueError as err:
    print("Read the f manual", err)
```

stones.py
```python
import itertools
from itertools import combinations, product
from sortedcontainers import SortedDict


def main():
    weights = SortedDict()
    stones = [1, 3, 9, 27]

    for stone in stones:
        for weight in weights.copy():
            weights[stone + weight] = sorted(weights[weight] + [stone])
            weights[stone - weight] = sorted([-w for w in weights[weight]] + [stone])

        weights[stone] = [stone]

    print(weights)



# def main():
#     weights = SortedDict(
#                 {
#                     sum([choice[i] * (3 ** i) for i in range(4)]): choice
#                     for choice in list(product([-1, 0, 1], repeat=4))
#                     if sum([choice[i] * (3 ** i) for i in range(4)]) > 0
#                 })
#
#     print(weights)

# def main():
#     weights = SortedDict()
#     ternary = [-1, 0, 1]
#     multipliers = [1, 3, 9, 27]
#
#     choices = list(product(ternary, repeat=4))
#
#     for choice in choices:
#         weight = sum([choice[i] * multipliers[i] for i in range(4)])
#
#         if weight < 0:
#             continue
#
#         weights[weight] = choice
#
#     print(weights)
#
#
# def main():
#     weights = {}
#     stones = [1, 3, 9, 27]
#
#     for number_left in range(1, 5):
#         for stones_left in combinations(stones, number_left):
#             stones_right = list(set(stones) - set(stones_left))
#
#             for number_right in range(0, len(stones_right) + 1):
#                 for counter_weight in combinations(stones_right, number_right):
#                     weight = sum(stones_left) - sum(counter_weight)
#
#                     if weight < 0:
#                         continue
#
#                     if weight in weights:
#                         print("This option exists already.")
#                         continue
#
#                     weights[weight] = (stones_left, counter_weight)
#
#     weights = dict(sorted(weights.items(), key=lambda item: item[0]))
#
#     print(len(weights))
#     print(weights)
#
if __name__ == "__main__":
    main()
```