from datetime import datetime

#def read_file2(filename):
#     """Read the file, process its content, and group letters by their occurrences."""
#     with open(filename, "r") as f:
#         # Read the contents of the file
#         content = ["".join(sorted(f.read().replace("\n", "").replace(" ", "")))]
#         for letter in content:
#
#
#     return content
# print(read_file2("words.txt"))

def read_file2(filename):
    """Read the file, process its content, and group letters by their occurrences."""
    with open(filename, "r") as f:
        # Read the contents of the file, remove newlines and spaces, then sort it
        content = sorted(f.read().replace("\n", "").replace(" ", ""))
        # Split the sorted content into individual letters

    return content

def group_letters(letters):
    """Group identical letters together into single strings and wrap in sublists."""
    grouped = []  # List to store grouped strings
    current_group = ""  # Temporary group for consecutive identical letters (as a string)

    for letter in letters:
        if not current_group or letter == current_group[-1]:
            # Add letter to the current group if it is the same as the last one
            current_group += letter
        else:
            # Append the current group as a list containing one string
            grouped.append([current_group])
            current_group = letter  # Start a new group with the current letter

    # Append the last group at the end
    lengths = []
    for string in grouped:
        lengths.append(len(string))

    print("Lengths:", lengths)

    return grouped



if __name__ == "__main__":

    start = datetime.now()

    # Process the file
    content = read_file2("words.txt")
    letters = group_letters(content)
    end = datetime.now()
    print("Time taken:", end - start)

    # Print the resulting grouped letters
    print("Grouped letters:", letters)

