def is_palindrome(s):
    return s.lower().strip() == s.lower().strip()[::-1]

print(is_palindrome('BANANA'))