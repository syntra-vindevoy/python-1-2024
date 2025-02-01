# theorie
# %% list to dict
list = [1, 2, 3, 4, 5]
some_dict = dict(list)
time
empty_dict = {}
empty_dict = dict()

copy_dict = dict(some_dict)

# %%

number_dict = {1: "one", 2: "two", 3: "three"}
if 1 in number_dict:
    print("1 is in the dictionary")

# %%
if "one" in number_dict:
    print("one is in the dictionary")

# %%
if "one" in number_dict.values():
    print("one is in the dictionary")
else:
    print("one is not in the dictionary")
# %%

print("ok") if "one" in number_dict.values() else print("nok")

# %%

word_dict = {"a": "apple", "b": "banana", "c": "cherry"}
for key in word_dict:
    print(key, word_dict[key])


# %%

import time


def reverse_word(word):
    return word[::-1]


def much_faster():
    count = 0
    for word in word_dict:
        if reverse_word(word) in word_dict:
            count += 1
        return count


# %%
# test this cell
from icecream import ic
import time


def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter


counter = value_counts("brontosaurus")
ic(counter)


# %%


some_dict = {"a": 1, "b": 2, "c": 3}

for key in some_dict:
    print(key, some_dict[key])

for value in some_dict.values():
    print(value)


# %%


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(100)

# %%

known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res


fibonacci(100)

# %%
