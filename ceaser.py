import string

def ceaser(word):
    c = ""
    for letter in word:
        if letter.isupper():
            i = (string.ascii_uppercase + string.ascii_uppercase).index(letter) + incr
            c+= string.ascii_uppercase[i]

    else:
        c += string.ascii_lowercase[string.ascii_lowercase.index(letter) + incr]
