"""Exercise 12.1. Write a function called most_frequent that takes a string and prints the let-
ters in decreasing order of frequency. Find text samples from several different languages and see
how letter frequency varies between languages"""

def letter_frequency(file_name):
    with open (file_name, "r") as f:
        words = f.read().lower()
    letters_count = {}
    for item in words:
        if item.isalpha():
            letters_count[item] = letters_count.get(item, 0) + 1

    letters_count = sorted(letters_count.items(), key=lambda item: item[1],reverse=True)
    letters = [letter for letter, count in letters_count]
    return letters
print (f"Dutch: {letter_frequency("text_nl.txt")}")
print(f"English: {letter_frequency("text_en.txt")}")
print(f"French: {letter_frequency("text_fr.txt")}")
