#Chapter 3 - Exercise 7

def square(f, g):
    f()
    for i in range(5):
        g()
    f()
    for i in range(5):
        g()
    f()

def outer():
    #print("+----+----+")
    print("+", "-" * 4, "+", "-" * 4, "+")

def inner():
    #print("|    |    |")
    print("/", " " * 4, "/", " " * 4, "/")

square(outer, inner)
