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

            # Skip if the current word is smaller than the longest_word already found
            if len(word) <= len(longest_word):
                continue

            if not has_duplicates(word):
                longest_word = word  # Update longest_word if the current word has no duplicates

    return longest_word


# Call the function with your file
filename = 'words.txt'  # Replace with the actual path if needed
longest_word = find_longest_word_without_duplicates(filename)
print("The longest word without duplicates is:", longest_word)


#CLASS OPTION
def has_duplicates_2(word: str) -> str:
    letters = {}

    for letter in word:
        if letter in letters:
            return True
        letters[letter] = True

# OR ONELINER

def has_duplicates_ol(word: str) -> bool:
    return len(word) > len(set(word))

with open("words.txt", "r") as file:
    words = file.read().splitlines()
    longest = 0
    longest_word_2 = ""

    for word in words:
        if len(word) < len(longest_word_2):
            continue

        if has_duplicates_2(word):
            continue

        if len(word) > longest:
            longest = len(word)
            longest_word_2 = word

print(longest_word_2, longest)

