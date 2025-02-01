# %%


def value_counts(word: str) -> dict:
    counter = {}
    for letter in word:
        counter[letter] = counter.get(letter, 0) + 1
    return counter


counter = value_counts("brontosaurus")
print(counter.get("b", 0))
print(counter.get("o", 0))

# %%


def has_duplicates(string: str) -> bool:
    """
    This function takes a string as input and returns True if there are any duplicates in the string.
    """
    return len(string) != len(set(string))
