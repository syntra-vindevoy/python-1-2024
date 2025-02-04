def count(word, letter):
    c = 0

    for w in word:
        if letter == w:
            c += 1

    return c


def lc_count(word, letter):
    return len([w for w in word if w == letter])


def one_liner_count(word, letter):
    return len(word) - len(word.replace(letter, ""))


assert one_liner_count("banana", "a") == 3
assert one_liner_count("banana", "n") == 2

assert lc_count("banana", "a") == 3
assert lc_count("banana", "n") == 2
