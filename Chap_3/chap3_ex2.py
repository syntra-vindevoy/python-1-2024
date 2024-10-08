# def triangle (char: str, height: int):
#     for i in range(1, height + 1):
#         # Calculating the number of characters and spaces needed for the current level
#         chars = char * (2 * i - 1)
#         spaces = ' ' * (height - i)
#         # Printing the current level of the pyramid
#         print(spaces + chars)
#
#
# # Example usage:
# triangle('L', 5)
#
# #van de leerkracht
#
# def triangle(char, number):
#     for i in range(number):
#         print(char * (i * 2 + 1))
#
# triangle("*", 6)
#
#
#
# def rectangle(char, width, height):
#     # Construct each line by repeating the character 'width' times
#     line = char * width
#
#     # Construct the entire rectangle by repeating the line 'height' times
#     result = "\n".join([line for _ in range(height)])
#
#     return result
#
#
# # Example usage
# if __name__ == "__main__":
#     print(rectangle('H', 5, 4))
#
# def rectangle(char, width, height):
#     if width < 2 or height < 2:
#         raise ValueError("Width and height must be at least 2.")
#
#     # Top and bottom lines
#     top_bottom = char * width
#
#     # Middle lines
#     middle = char + " " * (width - 2) + char
#
#     # Construct the entire rectangle
#     result = [top_bottom] + [middle for _ in range(height - 2)] + [top_bottom]
#
#     # Join all lines with newline character
#     return "\n".join(result)
#
#
# # Example usage
# if __name__ == "__main__":
#     print(rectangle('H', 5, 4))
from datetime import datetime

# def print_beam_with_posts(columns):
#     print(('+ ' + '- ' * box_size ) * columns + '+')
# #print(f"{(40 - len(text)) * ' '}{text}")
# def print_posts_with_spaces(columns):
#     print(('| ' + '  '* box_size ) * columns + '|')
#
#
# def print_row(columns):
#     print_beam_with_posts(columns)
#     for _ in range(4):
#         print_posts_with_spaces(columns)
#
#
# def print_grid(rows, columns, box_size):
#     for _ in range(rows):
#         print_row(columns, box_size)
#     print_beam_with_posts(columns)
#     print_box_size(box_size)
#
# print_grid(2, 2, box_size=4)

from datetime import datetime

start = datetime.now()
def print_beam_with_posts(columns, box_size):
    print(('+ ' + '- ' * box_size) * columns + '+')


def print_posts_with_spaces(columns, box_size):
    print(('| ' + '  ' * box_size) * columns + '|')


def print_row(columns, box_size):
    print_beam_with_posts(columns, box_size)
    for _ in range(box_size):
        print_posts_with_spaces(columns, box_size)


def print_grid(rows, columns, box_size):
    for _ in range(rows):
        print_row(columns, box_size)
    print_beam_with_posts(columns, box_size)

print_grid(2, 2, 5)

end= datetime.now()

time_diff = end - start

print(time_diff)

# def generate_beam(columns, box_size):
#     """Generate the string for a single beam row."""
#     return ('+ ' + '- ' * box_size) * columns + '+'
#
#
# def generate_post(columns, box_size):
#     """Generate the string for a single post row."""
#     return ('| ' + '  ' * box_size) * columns + '|'
#
#
# def print_grid(rows, columns, box_size):
#     """Print the entire grid."""
#     # Pre-generate row components to avoid repeated string concatenation
#     beam = generate_beam(columns, box_size)
#     post = generate_post(columns, box_size)
#
#     for _ in range(rows):
#         print(beam)
#         for _ in range(box_size):
#             print(post)
#     print(beam)  # Print the final beam at the bottom
#
#
# # Example usage
# if __name__ == "__main__":
#     print_grid(30, 30, 30)
#
# end= datetime.now()
#
# time_diff = end - start
#
# print(time_diff)