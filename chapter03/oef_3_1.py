def print_right(text, length):
    length_string = len(text)
    leading_spaces = (length - length_string) * " "

    print(f"{leading_spaces}{text}")

def triangle(letter, height):
    for i in range(height):
        print(f"{letter}{height}")

print_right("test", 40)

triangle("A", 3)
