import math

def mysqrt(a, x):
    while True:
        print(x)
        y = (x + a / x) / 2
        if y == x:
            break

        x = y

def mathsqrt(a):
    return math.sqrt(a)

def test_square_root(a):


def main():
    mysqrt(2,1)

if __name__ == "__main__":
    main()