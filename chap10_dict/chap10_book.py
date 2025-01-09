with open("words.txt", "r") as f:
    words = f.read().split("\n")

print(len(words))

def reverse_word(word):
    return ''.join(reversed(word))

def too_slow():
    count = 0
    for word in words:
        if reverse_word(word) in words:
            count += 1
    return count

print(too_slow())