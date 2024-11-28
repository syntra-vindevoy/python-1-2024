#Voodoo woord = als je de eerste letter van een woord neemt en het achteraan zet, is dit hetzelfde woord.
# Schrijf de isvoodoo functie

def is_voodoo(word: str) -> bool:
    return word[1:] == word[1:][::-1]

# Test cases
print(is_voodoo("ababa"))  # False (Moving the first 'a' to the end gives "ababa")
print(is_voodoo("voodoo")) # True (Moving the first 'v' to the end gives "voodoo")
print(is_voodoo("hello"))  # False (Moving the first 'h' to the end gives "elloh")
print(is_voodoo("madam"))  # False (Moving the first 'm' to the end gives "adamm")
