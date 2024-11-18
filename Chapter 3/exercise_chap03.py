# exercise 1 chap 03 false output
def print_right(text):
    text = text.strip()
    assert len(text) <= 40, "maximum length of text is 40 characters"
    return f"{' '*(40-len(text))}{text}"

def main():
    assert len(print_right("Geoffrey")) == 40
    assert print_right("Geoffrey")
    print(print_right("python"))
    print_right("user's always abuse your  system")

# exercise 2 chap 3 false output

def pyramid (character, height):
    for i in range(1, height + 1):
        num_chars = 2 * i - 1
        total_width = len(character) * num_chars
        spaces ='' * ((len(character) * height - total_width) // 2)
        row = character * num_chars
        print(spaces + row)
pyramid('*', 5)

# exercise 2 chap 3 good output

def triangle(char, height):
  for i in range(1, height + 1):
        # Calculate the number of spaces needed for centering
        num_chars = 2 * i - 1  # Number of repetitions of the string
        num_spaces = height - i  # Number of leading spaces to center the pyramid

        # Create the current row: spaces + repeated characters
        row = ' ' * num_spaces + char * num_chars

        # Print the row
        print(row)
triangle('°', 10)

# test return function

def check_even(number):
    return number % 2 == 0

print(check_even(7))

# exercise 3 chap 03

def rectangle (symb, height, width):
    for j in range(height):
        row = symb * width
        print(row)

rectangle('OK', 5, 5)

# exercise 3.1 uit thinkpython V2

n_spaces = 70

def right_justify(name, spaces):
    total = f'{(spaces * n_spaces) + name}'
    print(total)

right_justify('monty', ' ')

#exercise 3.2 uit thinkpython V2

def do_twice (f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)


# Exercise 3.3 uit thinkpython V2

aantal_horizontaal = 2
aantal_verticaal = 2

def rectangle_plus (plus, minus, horizminus, spatie):
        row1 = f'{(plus * 1) + (minus *  4) + (plus * 1)}'
        row2 = f'{(horizminus * 1) + (spatie * 4) + (horizminus * 1)}'
        print(row1 * aantal_horizontaal)
        for _ in range(4):
            print(row2 * aantal_horizontaal)
        print(row1 * aantal_horizontaal)

#for _ in range(aantal_verticaal):
    #rectangle_plus ('+', '-', '|')

for j in range (1,8):
    print (j, end= '')

