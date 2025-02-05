
def is_interlocking(word:str) -> bool:
    with open("words.txt", "r") as f:
        word_list = f.read().splitlines()

    words = {word for word in word_list}

    first = word[0::2]
    second = word[1::2]

    return first in words and second in words

print(is_interlocking("schooled"))
print(is_interlocking("brained"))
print(is_interlocking("planted"))