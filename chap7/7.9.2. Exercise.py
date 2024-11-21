def uses_none(word, letters):
    """Checks whether a word avoid forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
