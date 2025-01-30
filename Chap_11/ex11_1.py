def create_word_dict(file_path):
    """
    Reads words from a file and stores them as keys in a dictionary.

    Parameters:
        file_path (str): Path to the file containing words.

    Returns:
        dict: Dictionary with words as keys.
    """
    word_dict = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                word = line.strip()  # Remove any leading/trailing whitespace or newlines
                word_dict[word] = None  # Store the word as a key with a dummy value
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return word_dict


# Example usage:
# Assuming 'words.txt' is in the same directory and contains a list of words.
word_file = "words.txt"
word_dict = create_word_dict(word_file)

# Example of checking if a word is in the dictionary
word_to_check = "hell"
if word_to_check in word_dict:
    print(f"'{word_to_check}' is in the dictionary.")
else:
    print(f"'{word_to_check}' is not in the dictionary.")
