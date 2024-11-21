def uses_none(word, letters):
    """Checks whether a word avoids forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    """
    for letter in word.lower():

        if letter in letters.lower():

            return False  # A forbidden letter is found, so the word does not avoid the letters.

    return True

# Example usage
print(uses_none('kaka', 'xyz'))  # Should return True since 'xyz' are not in 'kaka'

# assert uses_none('banana', 'xyz') == True
# assert uses_none('apple', 'efg') == False