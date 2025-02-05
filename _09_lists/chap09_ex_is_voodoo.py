def is_voodoo(word:str) -> bool:
    return word[1::] == word[:0:-1]

print(is_voodoo("voodoo"))
print(is_voodoo("banana"))
print(is_voodoo("dresser"))
print(is_voodoo("thomas"))