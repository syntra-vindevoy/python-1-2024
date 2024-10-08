def rectangle(char, width, height):
    for i in range(height):
        # Print a row with the character repeated for the width of the rectangle
        print(char * width)

# Example usage:
rectangle('H', 5, 4)
