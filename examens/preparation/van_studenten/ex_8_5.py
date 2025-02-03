def caesar(word, shift):
    csr = ""

    for letter in word:
        offset = (ord("a") - ord("A")) * letter.isupper()
        lower = letter.lower()

        if ord(lower) + shift > ord("z"):
            csr += chr(ord("a") + ord("z") - ord(lower) + shift - offset - 1)
        else:
            csr += chr(ord(lower) + shift - offset)

    return csr


assert caesar("abc", 1) == "bcd"
assert caesar("xyz", 1) == "yza"

assert caesar("ABC", 1) == "BCD"
assert caesar("XYZ", 1) == "YZA"

assert caesar("abc", 2) == "cde"

assert caesar("aBcE", 2) == "cDeG"
