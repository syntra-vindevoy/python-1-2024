# exercise 1 chap 03 false output
from jinja2.idtracking import symbols_for_node
from numpy.ma.core import repeat


# def print_right(text):
#     text = text.strip()
#     assert len(text) <= 40, "maximum length of text is 40 characters"
#     return f"{' '*(40-len(text))}{text}"
#
# def main():
#     assert len(print_right("Geoffrey")) == 40
#     assert print_right("Geoffrey")
#     print(print_right("python"))
#     print_right("user's always abuse your  system")

# exercise 2 chap 3 false output

# def pyramid (char , height):
#     for i in range(1, height + 1):
#         num_chars = 2 * i - 1
#         total_width = len(char) * num_chars
#         spaces ='' * ((len(char) * height - total_width) // 2)
#         row = char * num_chars
#         print(spaces + row)
# pyramid('L', 5)

# exercise 2 chap 3 good output

# def triangle(char, height):
#   for i in range(1, height + 1):
#         # Calculate the number of spaces needed for centering
#         num_chars = 2 * i - 1  # Number of repetitions of the string
#         num_spaces = height - i  # Number of leading spaces to center the pyramid
#
#         # Create the current row: spaces + repeated characters
#         row = ' ' * num_spaces + char * num_chars
#
#         # Print the row
#         print(row)
# triangle('L', 9)

# test clarification return

# def check_even(number):
#     if number % 2 == 0:
#         return True  # Exits the function immediately if the condition is met
#     return False  # Only reached if the above condition was false
# print(check_even(7))

# exercise 3 chap 03

# def rectangle (symb, height, width):
#     for j in range(height):
#         row = symb * width
#         print(row)
#
# rectangle('OK', 5, 5)

def rectangle_plus (plus, minus, horizminus, spatie):
        row1 = f'{plus * 1}' + f'{minus *  4}' + f'{plus * 1}'
        row2 = f'{horizminus * 1}' + f'{spatie * 4}' + f'{horizminus * 1}'
        print(row1)
        for i in range(4):
            print(row2)
        print(row1)

for j in range(2):
    rectangle_plus ('+', '-', '|', ' ')


 #def rectangle_hor_line (symb2, horiz):


#def rectangle_minus (symb3, minus):