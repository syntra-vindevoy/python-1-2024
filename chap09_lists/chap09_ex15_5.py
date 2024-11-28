with open("words.txt", "r") as f:
    words = f.read().split("\n")

def total_length(word_list:list[str]) -> int:
    i = 0

    for word in word_list:
        i += len(word)

    return i

print(total_length(words))


with open("words.txt", "r") as f:
    words = f.read()

s = "".join(word.strip() for word in words.split())
print(len(s))


with open("words.txt", "r") as f:
    words = f.read().splitlines()

    s = sum([len(w) for w in words])
    print(s)