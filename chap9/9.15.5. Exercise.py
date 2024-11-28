#Write a function called total_length that takes a list of strings and returns the total length of the strings. The total length of the words in word_list should be
with open("words.txt", "r") as f:
    words = f.read().split("\n")

def total_length(words):
    return sum(len(word) for word in words)

print(total_length(words))