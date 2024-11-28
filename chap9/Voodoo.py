def is_voodoo(word: str) -> bool:
    return word[1:] == word[1:][::-1]