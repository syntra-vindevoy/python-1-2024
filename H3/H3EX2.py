def triangle(char, height):
    for i in range(1, height + 1):
        # Calculate leading spaces to center the pyramid
        spaces = ' ' * (height - i)

        # Repeat the character for the number of times needed in each row
        chars = char * (2 * i - 1)

        # Print each row with leading spaces
        print(spaces + chars)


# Example usage:
triangle('L', 5)
