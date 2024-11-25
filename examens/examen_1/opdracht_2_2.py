"""
Opdracht 2.2
author : Benoit Goethals
"""

import string


def verify_password(password):
    """
    Verify the strength of a password
    The algorithm is as follows:
    Length: 21 characters → 2 points
    Uppercase: Contains "A" → 3 points
    Lowercase: Contains "b" → 3 points
    Number: Contains "1" → 3 points
    Special character: Contains "!" → 4 points

    :param password: The password string to be verified.
    :return: An integer score representing the strength of the password based on its length, and the presence of upper case letters, lower case letters, digits, and special characters.
    """
    score = 0

    if len(password) >= 20:
        score += 2
    # check if any character in the password is an uppercase letter.
    if any(char in string.ascii_uppercase for char in password):
        score += 3
    # check if any character in the password is an lowercase letter.
    if any(char in string.ascii_lowercase for char in password):
        score += 3
    # check if any character in the password is an digit letter.
    if any(char.isdigit() for char in password):
        score += 3
    # Subtracts the set of ASCII letters and digits from the set of characters in the password.
    # This operation effectively removes all the letters and digits from the set,
    # leaving only the special characters.
    special_characters = set(password) - set(string.ascii_letters + string.digits)
    if len(special_characters) > 0:
        score += 4

    return score >= 15


assert verify_password("Abcdefghijklmnopqrstu1!") == True
assert verify_password("abcdefghijklmnopqrstu1!") == False
assert verify_password("BbcdefghIJjklmnopdfqrstu1$") == True
assert verify_password("Bbcdefghtu1$") == False
