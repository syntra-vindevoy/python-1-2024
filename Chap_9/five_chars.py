# import string
#
#
# def five_chars(s):
#     combinations = []
#     for l_1 in string.ascii_lowercase[:22]:
#         for l_2 in string.ascii_lowercase[1:23]:
#             for l_3 in string.ascii_lowercase[2:24]:
#                 for l_4 in string.ascii_lowercase[3:25]:
#                     for l_5 in string.ascii_lowercase[4:26]:
#                         combinations.append(l_1+l_2+l_3+l_4+l_5)
#
#     print("Number of combinations: ", len(combinations))
#     with open("words.txt", "r") as file:
#         words = file.read().splitlines()
#
#     print("Numbers of words: ", len(words))
#
# min_found = len(words)
# combo = []
#
#     for combination in combinations:
#         count_words = 0
#
#         for word in words:
#             found = False
#
#             for letter in combination:
#                 if letter in word:
#                     found = True
#
#             if not_found:
#                 count_words += 1
#
#         if count_words < min_found:
#             min_found = count_words
#             combo = combinations
#
from datetime import datetime

from datetime import datetime


def read_file(filename):
    """Read the file, process its content, and group letters by their occurrences."""
    with open(filename, "r") as f:
        # Read the contents of the file
        content = f.read()

        # Remove newline characters and spaces
        cleaned_content = content.replace("\n", "").replace(" ", "")

        # Create a dictionary to count letter occurrences
        grouped_letters = {}
        for letter in cleaned_content:
            if letter in grouped_letters:
                grouped_letters[letter] += 1
            else:
                grouped_letters[letter] = 1

        # Convert the dictionary into a list of tuples and sort it
        sorted_letters = sorted(grouped_letters.items(), key=lambda x: x[1])

    return sorted_letters


if __name__ == "__main__":
    start = datetime.now()

    # Process the file
    grouped_letters = read_file("words.txt")

    end = datetime.now()
    print("Time taken:", end - start)

    # Print the five least used letters
    print("Five least used letters:")
    for letter, count in grouped_letters[:2]:  # Using slicing to get the first 5 least used letters
        print(f"{letter}: {count}")


