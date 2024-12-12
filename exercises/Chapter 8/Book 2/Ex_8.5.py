import string

def ceasar(word, incr: int):

    c = ""

    for letter in word:
        if letter.isupper():
            i = string.ascii_lowercase.index(letter) + incr % 26
            c += string.ascii_uppercase[i]

        else:
            c += string.ascii_lowercase[string.ascii_lowercase.index(letter) + incr]


def ceasar2(word, incr: int):
    c = ""
    caps = string.ascii_uppercase + string.ascii_uppercase

    for letter in word:
        if letter.isupper():
            i = caps.index(letter) + incr
            c+= string.ascii_uppercase[i]

        else:
            c += string.ascii_lowercase[(string.ascii_lowercase.index(letter) + incr) % 26]