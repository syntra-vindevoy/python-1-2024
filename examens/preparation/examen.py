import string


def caesar2(word, incr: int):
    c = ""
    for letter in word:
        if letter.isupper():
            i = (string.ascii_uppercase.index(letter) + incr) % 26
            c += string.ascii_uppercase[i]
        elif letter.islower():
            i = (string.ascii_lowercase.index(letter) + incr) % 26
            c += string.ascii_lowercase[i]
        else:
            c += letter  # Leave non-alphabetic characters unchanged
    return c

assert caesar2("abc", 1) == "bcd"
assert caesar2("xyz", 1) == "yza"
assert caesar2("ABC", 1) == "BCD"
assert caesar2("XYZ", 1) == "YZA"
assert caesar2("abc", 2) == "cde"
assert caesar2("aBcE", 2) == "cDeG"
assert caesar2("cheer", 13) == "purre"
vowels = ["a", "e", "i", "o", "u"]
cities = ["Oudenaarde", "Opwijk", "Drongen", "Evergem", "Sint-Niklaas", "Gent", "Lede", "Dendermonde", "Wetteren",
          "Aalter", "Ursel"]
#must reverse
for t in cities[::-1]:
    if t in vowels:
        cities.remove(t)

steden = [stad for stad in cities if stad[0].lower() not in "aeuioy"]
print(steden)