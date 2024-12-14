def do_twice(f, a):
    f(a)
    f(a)

def print_twice(a):
    print(a)
    print(a)

def do_four(f, a):
    do_twice(f, a)
    do_twice(f, a)


if __name__ == "__main__":
    do_twice(print, 'spam')

    print()

    do_four(print, 'spam')

