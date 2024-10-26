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
        if letter not in available:
           return False
    return True
assert uses_only("banana", "ban") == True
assert uses_only("apple", "apl") == False


def uses_all(word, required):
    """Checks whether a word uses all required letters."""
    word = word.lower()
    required = required.lower()
    for letter in required:
        if letter not in word:
            return False
    return True
assert uses_all("banana", "ban") == True
assert uses_all("apple", "api") == False

