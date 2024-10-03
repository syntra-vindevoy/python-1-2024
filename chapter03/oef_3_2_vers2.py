def do_twice(func, text):
    func(text)
    func(text)

def print_spam(nr):
    print(nr)

def do_four(func, numb):
    pass

do_twice(print_spam,"spam")