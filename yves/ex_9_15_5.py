import sys
from datetime import datetime


with open("words.txt", "r") as f:
    words = f.read()

s = 0
for word in words:
    s += len(word.strip())

print(s)

with open("words.txt", "r") as f:
    words = f.read().splitlines()

    s = "".join(word for word in words)
    print(len(s))


with open("words.txt", "r") as f:
    words = f.read().splitlines()

    s = sum([len(w) for w in words])
    print(s)


with open("words.txt", "r") as f:
    words = f.read()

words = words.replace("\n", "")
print(len(words))


with open("words.txt", "r") as f:
    words = f.read()
    print(len(words) - words.count("\n"))
