def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("rotator"))

def is_voodoo(woord):
    return woord == (woord[1:] + woord[0])[::-1]
# voodoo kan je ook lezen, eerste letter niet belangrijk, is alles wat na de eerste letter komt een palindrome?


print(is_voodoo("voodoo"))

def is_annagram(woord_a, woord_b):
    return sorted(woord_a) == sorted(woord_b)

print(is_annagram("stop","post"))

