#deze is de juiste methode want sluit de file na ophaling
with open("words.txt", "r") as f:
    words = f.read().split("\n")

print(words)

"""
#volgende is niet de juiste methode: nooit gebruiken
f = open("words.txt", "r")
words = f.read().split("\n")
f.close()"""