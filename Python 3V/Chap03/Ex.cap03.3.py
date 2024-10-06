# Optie 1
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


# Optie 2
# def my_func1(line_length):
#     print("+", line_length * '-', '+', line_length * '-', '+', line_length * '-', '+')
#
# def my_func2(space_length):
#     for x in range(4):
#         print('/', space_length * ' ', '/', space_length * ' ', '/', space_length * ' ', '/')
#
# def total(line_length=4, space_length=4, num_rectangles=3):
#     for _ in range(num_rectangles):
#         my_func1(line_length)
#         my_func2(space_length)
#     my_func1(line_length)  # Zorg ervoor dat er aan het eind nog een onderste rand is
#
# # Voer de functie uit
# total(num_rectangles=6)  # Pas hier het aantal rechthoeken aan


#optie 3
# def draw_top_bottom_border(line_length):
#     """Teken de boven- en onderrand van de rechthoek."""
#     print("+" + line_length * '-' + "+" + line_length * '-' + "+" + line_length * '-' + "+")
#
# def draw_middle_space(space_length):
#     """Teken de ruimte tussen de randen van de rechthoek."""
#     for _ in range(2):  # Stel het aantal regels tussen de randen in op 4
#         print('|' + space_length * ' ' + '|' + space_length * ' ' + '|' + space_length * ' ' + '|')
#
# def draw_rectangles(line_length=5, space_length=5, num_rectangles=6):
#     """Teken een opgegeven aantal rechthoeken."""
#     for _ in range(num_rectangles):
#         draw_top_bottom_border(line_length)
#         draw_middle_space(space_length)
#     draw_top_bottom_border(line_length)  # Zorg ervoor dat er aan het eind nog een onderste rand is
#
# # Voer de functie uit met een aangepast aantal rechthoeken
# draw_rectangles(num_rectangles=5)  # Pas hier het aantal rechthoeken aan


# Optie 4
# def draw_top_bottom_border(line_length, num_rectangles):
#     """Teken de boven- en onderrand van de rechthoek."""
#     print("+" + (line_length * '-' + "+") * num_rectangles)
#
# def draw_middle_space(space_length, num_rectangles):
#     """Teken de ruimte tussen de randen van de rechthoek."""
#     for _ in range(2):  # Stel het aantal regels tussen de randen in op 2
#         print('|' + (space_length * ' ' + '|') * num_rectangles)
#
# def draw_rectangles(line_length=5, space_length=5, num_rectangles=3):
#     """Teken een opgegeven aantal rechthoeken."""
#     draw_top_bottom_border(line_length, num_rectangles)
#     draw_middle_space(space_length, num_rectangles)
#     draw_top_bottom_border(line_length, num_rectangles)  # Zorg ervoor dat er aan het eind nog een onderste rand is
#
# # Voer de functie uit met een aangepast aantal rechthoeken
#draw_rectangles(num_rectangles=5)  # Pas hier het aantal rechthoeken aan


# Optie 5
# def draw_top_bottom_border(line_length):
#     """Teken de boven- en onderrand van de rechthoek."""
#     print("+" + line_length * '-' + "+" + line_length * '-' + "+" + line_length * '-' + "+")
#
# def draw_middle_space(space_length):
#     """Teken de ruimte tussen de randen van de rechthoek."""
#     for _ in range(2):  # Stel het aantal regels tussen de randen in op 2
#         print('|' + space_length * ' ' + '|' + space_length * ' ' + '|' + space_length * ' ' + '|')
#
# def draw_rectangles(line_length=5, space_length=5, num_horizontal=3, num_vertical=2):
#     """Teken een opgegeven aantal rechthoeken horizontaal en verticaal."""
#     for _ in range(num_vertical):
#         for _ in range(num_horizontal):
#             draw_top_bottom_border(line_length)
#             draw_middle_space(space_length)
#         draw_top_bottom_border(line_length)  # Zorg ervoor dat er aan het eind nog een onderste rand is
#
# # Voer de functie uit met een aangepast aantal rechthoeken
#draw_rectangles(line_length=5, space_length=5, num_horizontal=4, num_vertical=1)  # Pas hier de aantallen aan

# Optie 6
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
draw_rectangles(line_length=3, space_length=3, num_horizontal=2, num_vertical=1)

# Optie docent


