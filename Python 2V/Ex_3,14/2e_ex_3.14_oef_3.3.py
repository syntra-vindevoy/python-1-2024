# Current Status: Complete

# This exercise can be done using only the statements and other features we
# have learned so far.

# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a comma-separated sequence: print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears
# on the same line.
# print '+',
# print '-'
# The output of these statements is '+ -'.
# A print statement all by itself ends the current line and goes to the next in
# line.
# 2. Use the previous function to draw a similar grid with four rows and four

# def my_func1():
#     print("+", 4*'-', '+', 4*'-', '+', 4*'-', '+')
#
# def my_func2():
#     for x in range(4):
#         print('|', 4*' ', '|', 4*' ', '|', 4*' ', '|')
#
# def total():
#     my_func1()
#     my_func2()
#     my_func1()
#     my_func2()
#     my_func1()
#     my_func2()
#     my_func1()
#
# total()

#Optie 2
def draw_top_bottom_border(line_length):
    """Teken de boven- en onderrand van de rechthoek."""
    return "+" + line_length * '-' + "+" + line_length * '-' + "+" + line_length * '-' + "+"


def draw_middle_space(space_length):
    """Teken de ruimte tussen de randen van de rechthoek."""
    space_line = '|' + space_length * ' ' + '|' + space_length * ' ' + '|' + space_length * ' ' + '|'
    return space_line + '\n' + space_line


def draw_rectangles(line_length=5, space_length=5, num_horizontal=3, num_vertical=2):
    """Teken een opgegeven aantal rechthoeken horizontaal en verticaal."""
    output = []

    for _ in range(num_vertical):
        output.append(draw_top_bottom_border(line_length))
        for _ in range(num_horizontal):
            output.append(draw_middle_space(space_length))
            output.append(draw_top_bottom_border(line_length))

    print('\n'.join(output))


# Voer de functie uit met een aangepast aantal rechthoeken
draw_rectangles(line_length=5, space_length=5, num_horizontal=3, num_vertical=1)


