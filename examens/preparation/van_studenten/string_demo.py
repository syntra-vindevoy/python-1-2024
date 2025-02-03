import string


def caesar(word, incr: int):
    c = ""
    caps = string.ascii_uppercase + string.ascii_uppercase
    for letter in word:
        if letter.isupper():
            i = caps.index(letter) + incr
            c += caps[i]


        elif letter.islower():
            c += string.ascii_lowercase[(string.ascii_lowercase.index(letter) + incr) % 26]

        else:
            c += letter

    return c


print(caesar("ABC", 1))

print(caesar("ROT13", 13))
