import string


# Define the Caesar cipher function
def caesar(word: str, incr: int):
    """
    Implements the Caesar cipher encryption method.
    Shifts each letter in the input string by a specified increment value.

    Parameters:
    - word (str): The string to be encrypted.
    - incr (int): The number of positions to shift each letter.

    Returns:
    - str: The encrypted string.
    """
    c = ""  # Initialize an empty string to store the encrypted result.
    caps = string.ascii_uppercase + string.ascii_uppercase
    # 'caps' stores uppercase letters doubled to handle wrap-around when shifting.

    for letter in word:  # Iterate over each character in the input string.
        if letter.isupper():  # Check if the letter is uppercase.
            # Find the current index of the letter, add the increment, and select the letter at the new position.
            i = caps.index(letter) + incr
            c += string.ascii_uppercase[i]  # Append the shifted letter to the result.  # Method 1

        elif letter.islower():  # Check if the letter is lowercase.
            # Find the index of the letter in uppercase (to handle the same position),
            # Shift by the increment value, and handle wrap-around using modulo operator.
            c += string.ascii_lowercase[(string.ascii_uppercase.index(letter) + incr) % 26]  # Method 2

        else:  # If the character is not a letter (e.g., spaces or punctuation).
            c += letter  # Directly append the character without encryption.

    return c  # Return the encrypted string.


# Example usage
print(caesar("ABC", 1))