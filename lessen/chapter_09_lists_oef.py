#maak een lijst met steden


#verwijder alle steden die beginnen met een klinker

# is een anagram, palindrome

# palindrome is woord dat omgekeerd hetzelfde is als voorwaarts
# anagram is woord met zelfde letters als een ander woord stop tops
# wat is een voodoo woord? voodoo is zelf een voodoo woord
# voodoo: eerste letter achteraan zetten en omgekeerd lezen is hetzelfde woord
# words.txt think python: alle woorden die in scrabble zijn toegelaten

def cities_without_vowels(cities, vowels):
    for c in cities.copy():
        if c[0].lower() in vowels:
            cities.remove(c)
        return cities

def cities_without_vowels_2(cities, vowels):
    return [c for c in cities if c[0].lower() not in vowels]



def cities_without_vowels_3(cities,vowels):
    for c in cities:
        if c[0].lower() in vowels:
            cities.remove(c)
    return cities


            
        








def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

def is_palindrome(word):
    return word == word[::-1]

def is_voodoo(word):
    return word[1:] + word[0] == word[::-1]




if __name__ == '__main__':

    cities = ['Oudenaarde','Zottegem','Sint-Niklaas','Kortrijk','Deinze','Gent','Erpe-Mere','Wetteren','Aalst','Aalter','Ninove']

    vowels = ['a','e','i','o','u']

    print(cities_without_vowels_2(cities,vowels)) # werkt niet
    #print(cities_without_vowels(cities, vowels))
    #print(cities_without_vowels_3(cities,vowels)) # werkt niet
    
    #print(cities)
    assert(is_anagram('seal','sale'))
    assert(is_palindrome('hanah'))
    assert(is_voodoo('voodoo'))