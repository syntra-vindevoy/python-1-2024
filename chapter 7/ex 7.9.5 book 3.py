def uses_all(word, required):
    """Checks whether a word uses all required letters."""
    word = word.lower()
    required = required.lower()
    for letter in required:
        if letter not in word:
            return False
    return True

def uses_only(word, available):
    """Checks whether a word uses only the available letters."""
    word = word.lower()
    available = available.lower()
    for letter in word:
        if letter not in available:
            return False
    return True

def check_word(word, available, required):
    """Check whether a word is acceptable."""
    word = word.lower()
    available = available.lower()
    required = required.lower()
    if len (word) < 4:
        return False
    if required not in word:
        return False
    return uses_only (word, available)

assert (check_word('color', 'ACDLORT', 'R')) == True
assert check_word('ratatat', 'ACDLORT', 'R') == True
assert check_word('rat', 'ACDLORT', 'R') == False
assert check_word('told', 'ACDLORT', 'R') == False
assert check_word('bee', 'ACDLORT', 'R') == False

def word_score(word, available):
    """Compute the score for an acceptable word."""
    if (uses_only(word, available) == False) or (len(word) < 4):
        return 0
    if len(word) == 4:
        return 1
    if uses_all(word, available):
        return 7 + len(word)
    return len(word)

assert word_score('card', 'ACDLORT') == 1
assert word_score('color', 'ACDLORT') == 5
assert word_score('cartload', 'ACDLORT') == 15
