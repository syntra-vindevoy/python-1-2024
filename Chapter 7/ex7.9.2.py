# Write a function named uses_none that takes a word and a string of forbidden letters
# and returns True if the word does not use any of the forbidden letters.

def uses_none(word: str, forbidden: str) -> bool:
    return not any(char in word for char in forbidden)

assert uses_none("sebastien", "zru") == True
assert uses_none("sebastien", "sb") == False
assert uses_none("sebastien", "x") == True

print(uses_none("sebastien", "xau"))
print(uses_none("sebastien", "zkl"))