def palindroome(word):
    return word == word[::-1]

print(palindroome('kayak'))
print(palindroome('radar'))

def anagram(word1, word2):
    return sorted(word1) == sorted(word2)

print(anagram('silent', 'lisent'))

def is_voodoo_word(word):
    return word[1:] == word[1:][::-1]
print(is_voodoo_word('voodoo'))

steden = [ "Oudenaarde", "Zottegem", "Sint-Niklaas", "Kortrijk" , "Gent",
           "Erpe-mere", "Aalst", "Ninove", "Opwijk", "Lede"]


for stad in steden[::-1]:
    begin = stad[0].lower()

    if begin in "aeuioy":
        steden.remove(stad)
print(steden)

steden = [stad for stad in steden if not stad[0].lower() in "aeuioy"]

print(steden)



