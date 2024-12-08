def generate_squares(n):
    for i in range(n):
        yield i**2 # yield is a keyword that is used like return, except the function will return a generator



def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b



if __name__ == "__main__":
    for square in generate_squares(10):
        print(square)


    # Create a generator object
    fib_gen = fibonacci()

    # Generate and print the first 10 Fibonacci numbers
    for _ in range(10):
        print(next(fib_gen))