def do_twice(f, t):
    f(t)
    f(t)


def print_spam(t):
    print(t)


if __name__ == "__main__":
    do_twice(print_spam, "spam")
