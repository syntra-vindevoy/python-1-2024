def is_palindrome(word:str) -> bool:
    return word == word[::-1]

print(is_palindrome("kayak"))
print(is_palindrome("noon"))
print(is_palindrome("thomas"))