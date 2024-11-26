def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

print(is_anagram("leven", "elven"))
print(is_anagram("leven", "kerel"))