#Chapter 3 - Exercise 8
def square(x, y, z, f, g):
    for i in range(y):
        f(x, z)
        for j in range(z):
            g(x, z)
    f(x, z)

def pattern1(x, z):
    #part = "+" + "-" * z
    #side = part * x + "+"
    #print(side)
    print((("+" + "-" * z) * x) + "+")

def pattern2(x, z):
    #part = "|" + " " * z
    #side = part * x + "|"
    #print(side)
    print((("|" + " " * z) * x) + "|")

square(4, 4, 4, pattern1, pattern2)
square(5, 2, 5, pattern1, pattern2)
square(10, 3, 3, pattern1, pattern2)
