def count(word, letter):
    c = 0

    for w in word:
        if letter == w:
            c += 1

    return c


def one_liner_count(word, letter):
    return len(word) - len(word.replace(letter, ""))


assert one_liner_count("banana", "a") == 3
assert one_liner_count("banana", "n") == 2

