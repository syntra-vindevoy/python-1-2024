import math

def newton_square(a):
    x = int(input("What's your estimate?"))
    epsilon = 0.0000000001
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            return y
        x = y


def test_square_root(a):
     print(a, newton_square(a), math.sqrt(a), abs((newton_square(a) - math.sqrt(a))))

test_square_root(4222)