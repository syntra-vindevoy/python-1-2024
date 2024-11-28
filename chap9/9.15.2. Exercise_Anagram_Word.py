with open("words.txt", "r") as f:
    words = f.read().split("\n")

print(words)
print(type(words))

f = open("word.txt", "r")
words = f.read().split("\n")
f.close()