#Chapter 3 - Exercise 6

def do_twice(f):
    f()
    f()

def print_test():
    print("Test")

do_twice(print_test)