def uses_none(word, forbidden):
    """Checks whether a word avoids forbidden letters.

    #>>> uses_none('banana', 'xyz')
    True
    #>>> uses_none('apple', 'efg')
    False
    #>>> uses_none('', 'abc')
    True
    """
    return not uses_any(word, forbidden)