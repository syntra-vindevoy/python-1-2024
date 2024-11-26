#remove all cities which start with a vowel
steden = ["oudenaarde", "zottegem", "sint-niklaas", "kortrijk", "deinze", "gent", "lede", "erpe-mere", "wetteren", "aalst", "ninove", "aalter", "opwijk"]
print(steden)

def is_vowel(char:str) -> bool:
    return char in "aeiouyAEIOUY"

i = len(steden)
while i > 0:
    i -= 1
    if is_vowel(steden[i][0]):
        steden.pop(i)

print(steden)