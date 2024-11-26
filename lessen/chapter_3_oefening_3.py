
def print_square(width):
    count = (width - 3) // 2
    print_special_line(count)
    print_normal_lines(count)
    print_special_line(count)
    print_normal_lines(count)
    print_special_line(count)


def print_normal_lines(count):
    for i in range(count):
        print_normal_line(count)


def print_normal_line(count):
    print(f"|{" "*count}|{" "*count}|")


def print_special_line(count):
    print(f"+{"-"*count}+{"-"*count}+")


print_square(9)

