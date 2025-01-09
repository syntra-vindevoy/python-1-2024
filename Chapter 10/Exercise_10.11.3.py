#What is the longest word you can think of where each letter appears only once?
#Let’s see if we can find one longer than unpredictably.

#Write a function named has_duplicates that takes a sequence – like a list or string
#– as a parameter and returns True if there is any element that appears in the sequence more than once.

def has_duplicates(sequence):
    counter = {}
    for item in sequence:
        if item in counter:
                return True
        counter[item] = 1
    return False


def find_longest_word_without_duplicates(filename):
    longest_word = ""

    # Open the file containing the words
    with open(filename, 'r') as file:
        words = file.readlines()  # Read all lines (words) into a list

        for word in words:
            word = word.strip()  # Remove any leading/trailing whitespace or newline characters

            if not has_duplicates(word) and len(word) > len(longest_word):
                longest_word = word  # Update longest_word if the current word is longer and has no duplicates

    return longest_word


# Call the function with your file
filename = 'words.txt'  # Replace with the actual path if needed
longest_word = find_longest_word_without_duplicates(filename)
print("The longest word without duplicates is:", longest_word)