def print_right(text, length):
    length_string = len(text)
    leading_spaces = (length - length_string) * " "

    print(f"{leading_spaces}{text}")

print_right("test", 40)
