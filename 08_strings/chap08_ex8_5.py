import string



def caesar(word:str, incr:int):
    c = ""
    caps = string.ascii_uppercase + string.ascii_uppercase

    for letter in word:
        if letter.isupper():
            i = caps.index(letter) + incr
            c += string.ascii_uppercase[i]                                                      #Method 1

        elif letter.islower():
            c += string.ascii_lowercase[(string.ascii_uppercase.index(letter) + incr) % 26]     #Method 2

        else:
            c += letter

    return c

print(caesar("ABC", 1))