import random

# %%
# ask an assistant

# %%
# Exercise 1: method called get


def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter


counter = value_counts("brontosaurus")
b = "b", counter.get("b", 0)
print(b)
s = "s", counter.get("s", 0)
print(s)
x = "x", counter.get("x", 0)
print(x)


# %%
"""
What is the longest word you can think of where each letter appears only once? Let's see if we can find one longer than unpredictably.
Write a function named has_duplicates that takes a sequence -- like a list or string -- as a parameter and returns True if there is any element that appears in the sequence more than once.
To get you started, here's an outline of the function with doctests.
"""


def has_duplicates(string):
    if len(string) == len(set(string)):
        return False
    else:
        return True


assert has_duplicates("test") == True
assert has_duplicates("no") == False

print("all asserts passed")

# %%

some_list = [1, 2, 3, 5, 5, 6, 7, 8, 9, 10]
some_list = [random.randint(1, 20) for _ in range(100)]

def find_repeats(string):

        
