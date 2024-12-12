import string

def caesar(word, incr: int):
    c = ""
    for letter in word:
        if letter.isupper():
            c += string.ascii_uppercase[string.ascii_uppercase.index(letter) + incr]
        else:
            c += string.ascii_uppercase [string.ascii_lowercase.index(letter) + incr]

caesar("top", 3)