with open("words.txt", "r") as f:
    words = f.read().split("\n")

def total_length(word_list:list[str]) -> int:
    i = 0

    for word in word_list:
        i += len(word)

    return i

print(total_length(words))