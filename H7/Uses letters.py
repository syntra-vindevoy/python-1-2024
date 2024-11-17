def has_e(word):
    return 'e' in word.lower()

print(has_e('pan'))

def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False

print(uses_any('banana', 'aeiou'))
print(uses_any('apple', 'xyz'))

