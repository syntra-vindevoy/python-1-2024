# maak een lijst met steden
from datetime import datetime
import sys

# verwijder alle steden die beginnen met een klinker

# is een anagram, palindrome

# palindrome is woord dat omgekeerd hetzelfde is als voorwaarts
# anagram is woord met zelfde letters als een ander woord stop tops
# wat is een voodoo woord? voodoo is zelf een voodoo woord
# voodoo: eerste letter achteraan zetten en omgekeerd lezen is hetzelfde woord
# words.txt think python: alle woorden die in scrabble zijn toegelaten


def cities_without_vowels_1(cities, vowels):
    for city in cities[::-1]:
        if city[0].lower() in vowels:
            cities.remove(city)
    return cities


def cities_without_vowels_2(cities, vowels):
    return [c for c in cities if c[0].lower() not in vowels]


def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


def is_palindrome(word):
    return word == word[::-1]


def is_voodoo(word):
    return word[1:] == word[1:][::-1]


def is_voodoo_2(word):
    return word[1:] + word[0] == word[::-1]


def with_open():
    with open("words.txt", "r") as f:
        words = f.read().split("\n")
    start = datetime.now()

    for word in words:
        if is_anagram(word, "takes"):
            print(word)
    end = datetime.now()
    print(end - start)


def without_open():
    f = open("words.txt", "r")
    words = f.read().split("\n")
    f.close()
    print(words)


def character_count(filename):
    with open(filename, "r") as f:
        text = f.read()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


if __name__ == "__main__":

    print(character_count("words.txt"))

    sys.exit()
    with_open()

    cities = [
        "Oudenaarde",
        "Zottegem",
        "Sint-Niklaas",
        "Kortrijk",
        "Deinze",
        "Gent",
        "Erpe-Mere",
        "Wetteren",
        "Aalst",
        "Aalter",
        "Ninove",
    ]
    vowels = ["a", "e", "i", "o", "u"]

    print(cities_without_vowels_1(cities, vowels))
    print(cities_without_vowels_2(cities, vowels))  # werkt niet

    # print(cities)
    assert is_anagram("seal", "sale")
    assert is_palindrome("hanah")
    assert is_voodoo("voodoo")
