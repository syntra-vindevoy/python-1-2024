#remove all cities which start with a vowel
steden = ["oudenaarde", "zottegem", "sint-niklaas", "kortrijk", "deinze", "gent", "lede", "erpe-mere", "wetteren", "aalst", "ninove", "aalter", "opwijk"]
print(steden)

def is_vowel(char:str) -> bool:
    return char in "aeiouAEIOU"
print(len(steden))

for i in range((len(steden) - 1)):
    stad = steden[i]
    letter = stad[0]
    print(stad, letter)
    if is_vowel(letter):
        print(i)

print(steden)