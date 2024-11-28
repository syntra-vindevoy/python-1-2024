#Write a function called total_length that takes a list of strings and returns the total length of the strings.
# The total length of the words in word_list should be 902.728

with open("words.txt") as f:
    words = f.read().split("\n") #split so it removes the "\n" characters

def total_length(words):
    total = 0
    for word in words:
        total += len(word)
    return total
print(f"Total length of words: {total_length(words)}")