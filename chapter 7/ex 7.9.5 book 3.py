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
