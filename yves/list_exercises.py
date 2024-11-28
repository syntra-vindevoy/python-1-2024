def is_anagram(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)

def is_palindrome(word: str) -> bool:
    return word == word[::-1]

def is_voodoo(word: str) -> bool:
    return word[1:] == word[1:][::-1]

assert is_voodoo("voodoo")
assert is_voodoo("voo")
assert not is_voodoo("oov")


steden = ["Brussel", "Oudenaarde", "Zottegem", "Opwijk", "Sint-Niklaas", "Kortrijk", "Deinze", "Gent", "Aalst",
          "Erpe-Mere", "Ninove"]

for stad in steden[::-1]:
    print("Ik controleer", stad)
    begin = stad[0].lower()

    if begin in "aeuioy":
        print("Ik verwijder ", stad)
        steden.remove(stad)

print(steden)