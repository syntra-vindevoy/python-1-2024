letters = "abcdefghijklmnopqrstuvwxyz"
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))

print(letter_map["a"])


def shift_word(word, shift):
    return "".join([letters[(letter_map[letter] + shift) % 26] for letter in word])


assert shift_word("abc", 1) == "bcd"
assert shift_word("xyz", 3) == "abc"
assert shift_word("abc", 0) == "abc"
assert shift_word("cheer", 7) == "jolly"
