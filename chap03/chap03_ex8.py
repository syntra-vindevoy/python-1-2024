#Chapter 3 - Exercise 8
def square(x, y, z, f, g):              #Another option would have been to define functions pattern1 & 2 inside the function square
    for _ in range(y):                  #Similar like a variable who's declared inside a function, the def in a def is local
        f(x, z)                         #Technically it was not necessary to add "f" and "g" as parameter to def square
        for _ in range(z):              #def pattern1 & 2 could just be called in the def square without it being in the parameters
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
