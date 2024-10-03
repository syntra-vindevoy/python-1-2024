# A function object is a value you can assign to a variable or pass as an argument. For
# example, do_twice is a function that takes a function object as an argument and calls it twice:

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)