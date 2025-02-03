def edge_line(horizontal, size):
    r = "+"
    r += ("-" * size + "+") * horizontal

    return r


def vol_line(horizontal, size):
    r = "|"
    r += (" " * size + "|") * horizontal

    return r


def squares(horizontal, vertical, size):

    for _ in range(vertical):
        print(edge_line(horizontal, size))

        for _ in range(size):
            print(vol_line(horizontal, size))

    print(edge_line(horizontal, size))


squares(5, 4, 3)
