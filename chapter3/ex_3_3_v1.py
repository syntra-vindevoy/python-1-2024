def do_twice(f):
    f()
    f()


def do_four(f, p):
    f(p)
    f(p)
    f(p)
    f(p)


def print_char(c):
    print(c, end=" ")


def horizontal_line():
    print_char("+")
    do_four(print_char, "-")
    print_char("+")
    do_four(print_char, "-")
    print_char("+")
    print()


def vertical_line(_):
    print_char("|")
    do_four(print_char, " ")
    print_char("|")
    do_four(print_char, " ")
    print_char("|")
    print()


def boxes():
    horizontal_line()
    do_four(vertical_line, None)
    horizontal_line()
    do_four(vertical_line, None)
    horizontal_line()


if __name__ == "__main__":
    boxes()
