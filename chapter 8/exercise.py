import string
a = "banana"
print (a.count("a"))

def is_palindrome(word):
    return word.upper() == word[::-1].upper()
#print (is_palindrome("odo"))

print (ord("a"))
print (chr(98))

def ceasar(word, incr : int):
    c = ""
    for letter in word:
        if letter.isupper():
            i = (string.ascii_uppercase.index(letter) % 26)
            c += string.ascii_uppercase[i]
        else:
            c += string.ascii_lowercase[string.ascii_lowercase.index(letter) + incr]


def ceasar2 (word, incr : int):
    c = ""
    caps = string.ascii_uppercase + string.ascii_uppercase
    for letter in word:
        if letter.isupper():
            i = caps.index(letter) + incr
            c += string.ascii_uppercase[i]
        else:
            c += string.ascii_lowercase[(string.ascii_lowercase.index(letter) + incr) % 26]
    return c

print (ceasar2("aot", -2))





