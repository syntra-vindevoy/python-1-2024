import math

def newton_square(a, x):
    epsilon = 0.0000000001

    while True:
        y = (x + a/x) / 2

        if abs(y-x) < epsilon:
            return y

        x = y


def execute_test(a, b):
    nq = (newton_square(a, b))
    mq = math.sqrt(a)

    print(a, nq, mq, abs(nq - mq))


def test_square_root():
    a = int(input("What is your number to calculate the square root?  "))
    b = int(input("What do you think it is approximately?  "))

    execute_test(a, b)


if __name__ == "__main__":
    # test_square_root()

    for i in range(1, 10):
        execute_test(i, i/2)
