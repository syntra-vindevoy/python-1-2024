def read_file_line_by_line(file_path):
    """
    Generator function to read a file line by line.
    Yields each line of the file as a string.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()  # Strip removes newline characters
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    file_path = "words.txt"  # Replace with your file path

    print(f"Reading file: {file_path}\n")
    for line in read_file_line_by_line(file_path):
        print(line)
hè
