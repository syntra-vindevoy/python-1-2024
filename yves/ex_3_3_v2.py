box_size = 5


def n_times(n, f, p):
    if n > 0:
        f(p)
        n_times(n - 1, f, p)


def print_char(c):
    print(c, end=" ")


def horizontal_part(_):
    n_times(box_size, print_char, "-")
    print_char("+")


def horizontal_line():
    print_char("+")
    n_times(2, horizontal_part, None)
    print()


def vertical_part(_):
    n_times(box_size, print_char, " ")
    print_char("|")


def vertical_line(_):
    print_char("|")
    n_times(2, vertical_part, None)
    print()


def boxes():
    horizontal_line()
    n_times(box_size, vertical_line, None)
    horizontal_line()
    n_times(box_size, vertical_line, None)
    horizontal_line()


if __name__ == "__main__":
    boxes()
