import math

def mysqrt (a):
    x = a/5
    while True:
        print(x)
        x = a/5
        y = (x + a/x) / 2
        if y == x:
            return x
        break
x = y

#def test_square_root (table):

