#Chapter 3 - Exercise 3

def triangle(text, h):
    for i in range(1, h + 1):
        print(text * i)

triangle("L", 5)
triangle("A", 5)


def rectangle(text, b, h):
    for i in range(1, h + 1):
        print(text * b)

rectangle("H", 5, 4)