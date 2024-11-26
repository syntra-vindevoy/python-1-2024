#A palindrome is a word that is spelled the same backward and forward, like “noon” and “rotator”.
# Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise.

#You can use the following loop to find all of the palindromes in the word list with at least 7 letters.
def is_palindrome(word: str) -> bool:
    return word == ''.join(reversed(word))

assert is_palindrome("lepel") == True
assert is_palindrome("koets") == False
assert is_palindrome("rotator") == True


def is_palindrome_2(word: str) -> bool:
    return word == word[::-1]

assert is_palindrome_2("lepel") == True
assert is_palindrome_2("koets") == False
assert is_palindrome_2("rotator") == True


