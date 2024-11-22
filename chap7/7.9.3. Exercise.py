def uses_only(word, available):
    """Checks whether a word uses only the available letters.

    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    """
    for letters in word.lower():

        if letters not in available.lower():

            return False

    return True

print (uses_only('apple', 'apl'))
print(uses_only('banana', 'ban'))  # True (all letters in 'banana' are in 'ban')
print(uses_only('apple', 'apl'))   # False ('e' is not in 'apl')
print(uses_only('cat', 'cat'))     # True (exact match)
print(uses_only('dog', 'cat'))     # False ('d', 'o', and 'g' are not in 'cat')