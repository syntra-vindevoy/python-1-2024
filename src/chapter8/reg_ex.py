import re
from re import Match

def count_matches(lines: str, pattern: str) -> int:
    return sum(1 for line in lines if re.search(pattern, line))


# Function to find the first match of a pattern in a list of lines.
def find_first(lines: str, pattern: str) -> Match[str]:
    for line in lines:
        # Search for the pattern in each line.
        result = re.search(pattern, line)
        # If a match is found, return the match object.
        if result is not None:
            return result



def main():
    # Input text to search patterns within.
    text = "I am Dracula; and I bid you welcome, Mr. Harker, to my house."
    # Pattern to match 'Dracula' within the text.
    pattern = 'Dracula'

    # Search for the pattern 'Dracula' in the text using regular expressions.
    result = re.search(pattern, text)

    # Print the match object (if any), the original text, the matched pattern, and its span (start and end indices).
    print(result)  # Prints the match object
    print(result.string)  # Prints the original text being searched
    print(result.group())  # Prints the found match (the word 'Dracula')
    print(result.span())  # Prints the starting and ending indices of the match
    print("---------------")
    # Attempt to search for the word 'Count' in the text.
    result = re.search("Count", text)

    # Print the result of the search; this will return `None` because 'Count' is not in the text.
    print(result)  # Prints None if 'Count' is not found
    print(result == None)  # Check if the result is None (True if pattern not found)
    print("---------------")
    # Read the contents of a file (pg345.txt) line by line into a list of lines.
    with open("pg345.txt", encoding="utf-8") as f:
        lines = f.readlines()

    # Find and return the first line containing the pattern 'Harker'.
    result = find_first(lines, "Harker")
    print(result.string)  # Print the line containing the first encounter of 'Harker'

    # Define a pattern to search for names 'Mina' or 'Murray'.
    pattern = "Mina|Murray"
    result = find_first(lines, pattern)
    print(result.string)  # Print the line containing the first encounter of 'Mina' or 'Murray'

    # Define a new pattern that matches any of 'Harker', 'Mina', or 'Murray'.
    pattern = "Harker|Mina|Murray"
    result = find_first(lines, pattern)
    print(result.string)  # Print the line containing the first encounter of any of these names
    print("---------------")

    # Define a pattern for 'Mina' or 'Murray' and count the occurrences in all the lines.
    pattern = "Mina|Murray"
    print(count_matches(lines, pattern))  # Print the count of lines containing either 'Mina' or 'Murray'

    # Define a pattern to find lines starting with the word 'Dracula'.
    pattern = "^Dracula"
    print(find_first(lines, pattern).string)  # Print the first line starting with 'Dracula'

    # Define a pattern to find lines ending with 'Harker'.
    pattern = "Harker$"
    print(find_first(lines, pattern).string)  # Print the first line ending with 'Harker'

    pattern = "cent(er|re)"
    result = find_first(lines, pattern)
    print(result.string)


    pattern = "colou?r"
    result = find_first(lines, pattern)
    line = result.string
    print(line)


    line = re.sub(pattern, "color", line)
    print(line)

if __name__ == "__main__":
    main()



