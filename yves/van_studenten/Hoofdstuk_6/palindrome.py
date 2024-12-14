def is_palindrome(s):
    return s.lower().strip() == s.lower().strip()[::-1]

s = input("What word?")

print(is_palindrome(s))