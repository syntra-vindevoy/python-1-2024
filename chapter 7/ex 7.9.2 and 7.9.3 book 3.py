def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters."""
    word = word.lower()
    forbidden = forbidden.lower()
    for letter in forbidden:
        if letter in word:
            return False
    return True

assert uses_none("banana", "xyz") == True
assert uses_none("apple", "efg") == False

def uses_only(word, available):
    """Checks whether a word uses only the available letters."""
    word = word.lower()
    available = available.lower()
    for letter in word:
        if letter in available:
            None
        else:
            return False
    return True
assert uses_only("banana", "ban") == True
assert uses_only("apple", "apl") == False
