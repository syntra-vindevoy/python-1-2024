# Exercise 9.2. In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter “e”.
# Since “e” is the most common letter in English, that’s not easy to do.
# Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.

with open('words.txt', 'r') as file:
    words = [line.strip() for line in file]

def has_no_letter_e(word):
    return "e" not in word  # The condition itself returns a Boolean

assert has_no_letter_e("banana") == True
assert has_no_letter_e("elf") == False


# Write a program that reads words.txt and prints only the words that have no “e”.

# Open the file and read all lines into a list
def print_words_with_e(words):
    for word in words:
        if "e"  not in word:
            print(word)

print_words_with_e(words)

# Compute the percentage of words in the list that have no “e”.
def percentage_of_no_e_words(words):
    total_words = len(words)
    words_without_e = 0
    for word in words:
        if "e" not in word:
            words_without_e += 1

    percentage = words_without_e / total_words * 100
    print(f"The percentage of words without 'e' in the list words.txt is {percentage:.2f}%")

percentage_of_no_e_words(words)
