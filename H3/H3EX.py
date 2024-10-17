def print_right(text):
    # Calculate the number of leading spaces needed
    total_columns = 40
    text_length = len(text)
    leading_spaces = total_columns - len(text)

    # Print the text with leading spaces
    if leading_spaces > 0:
        print(' ' * leading_spaces + text)
    else:
        print(text)  # If the text is longer than 40 columns, just print it


# Example usage:
print_right("Hello, World!")
