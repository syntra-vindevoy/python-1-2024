# Write a function called uses_only that takes a word and a string of letters
# and that returns True if the word contains only letters in the string.

def uses_only(word, available):
    """Checks whether a word uses only the available letters.
    uses_only('banana', 'ban')
    True
     uses_only('apple', 'apl')
    False
    """
    return all(char in available for char in word)
    return None

print(uses_only('banana', 'ban'))
print(uses_only('apple', 'apl'))
print(uses_only('sebastien', 'nitabes'))