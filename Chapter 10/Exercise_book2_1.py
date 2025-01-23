#Exercise 11.1. Write a function that reads the words in words.txt
#and stores them as keys in a dictionary. It doesn’t matter what the values are.
#Then you can use the in operator as a fast way to check whether a string is in the dictionary.

def create_word_dict(filename):
    word_dict = {}

    # Open the file and read the words
    with open(filename, "r") as file:
        words = file.read().splitlines()  # Read all words as a list

        # Store words as keys in the dictionary (values don't matter)
        for word in words:
            word_dict[word] = None  # Store each word with a placeholder value (None)

    return word_dict

# Example usage
filename = "words.txt"  # Your file
word_dict = create_word_dict(filename)

# Example of checking if a word exists in the dictionary using the 'in' operator
word_to_check = "ambidextrously"  # Replace with the word you want to check
if word_to_check in word_dict:
    print(f"'{word_to_check}' exists in the dictionary.")
else:
    print(f"'{word_to_check}' does not exist in the dictionary.")



