box_size = 4


def n_times(n, f, *p):
    if n > 0:
        if p is None:
            f()
        else:
            f(*p)

        n_times(n - 1, f, *p)


def print_char(c):
    print(c, end=" ")


def part(c, e):
    n_times(box_size, print_char, c)
    print_char(e)


def line(c, f, *p):
    print_char(c)
    n_times(2, f, *p)
    print()

def boxes():
    line("+", part, "-", "+")
    n_times(box_size, line, "|", part, " ", "|")
    line("+", part, "-", "+")
    n_times(box_size, line, "|", part, " ", "|")
    line("+", part, "-", "+")


if __name__ == "__main__":
    boxes()
