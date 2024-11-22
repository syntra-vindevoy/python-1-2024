def check_word(word, available, required):
    """Check whether a word is acceptable.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    # Ensure the word length is at least 4

    if len(word) < 4:

        return False

    # Check each letter in the word
    for letter in word.upper():

        if letter not in available:

            return False  # If a letter is not in available, return False

    # Check if the required letter is in the word
    if required.upper() not in word.upper():

        return False


    return True


# Example usage
print(check_word('color', 'ACDLORT', 'R'))     # True
print(check_word('ratatat', 'ACDLORT', 'R'))  # True
print(check_word('rat', 'ACDLORT', 'R'))      # False
print(check_word('told', 'ACDLORT', 'R'))     # False
print(check_word('bee', 'ACDLORT', 'R'))      # False
