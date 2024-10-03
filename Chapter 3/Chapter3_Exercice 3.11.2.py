# Write a function named print_right that takes a string named text as a parameter and prints the string
# with enough leading spaces that the last letter of the string is in the 40th column of the display.
# Hint: Use the len function, the string concatenation operator (+) and the string repetition operator (*).

def print_right(text):
    text = text.strip() # This removes "empty" characters from the returned string

    assert len(text) <= 40, "Maximum length of text is 40 characters"

    # This prints a formatted string that displays (40 - the length of the string) * a space and follows with the string
    return f"{(40-len(text))*' '}{text}"

def main():
    print(print_right("Hello World"))
    print(print_right("Sébastien"))
    print(print_right("Soep"))
    print(print_right("12345678911234567891123456789112345678912")) # Error message test

if __name__ == "__main__":
    main()
