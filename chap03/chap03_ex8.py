#Chapter 3 - Exercise 8

def square(x, y, z, f, g):
    for i in range(y):
        f(x, z)
        for j in range(z):
            g(x, z)
    f(x, z)

def outer(x, z):
    part = "+" + "-" * z
    side = part * x + "+"
    print(side)
    #print("+", "-" * 4, "+", "-" * 4, "+")

def inner(x, z):
    part = "|" + " " * z
    side = part * x + "|"
    print(side)
    #print("/", " " * 4, "/", " " * 4, "/")

square(4, 4, 4, outer, inner)
square(5, 2, 5, outer, inner)
square(10, 3, 3, outer, inner)
