def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
            print(c)


def check_numbers():
    n = int(input("What is the number you want the Fibonacci sequence of?"))
    fibonacci(n)

check_numbers()
