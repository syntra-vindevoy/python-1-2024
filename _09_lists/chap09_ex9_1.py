with open("words.txt", "r") as f:
    words = f.read().split("\n")

for word in words:
    if len(word) > 20:
        print(word)