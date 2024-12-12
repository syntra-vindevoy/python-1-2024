#Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace).

# Open the file and read all lines into a list
with open('words.txt', 'r') as file:
    words = [line.strip() for line in file]

# Function to print words with more than 20 characters
def plus_20_chars(words):
    for word in words:
        if len(word) > 20:  # Check if the word has more than 20 characters
            print(word)

# Call the function with the list of words
plus_20_chars(words)
