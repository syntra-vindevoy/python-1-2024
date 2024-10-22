def fibonacci(n):
    # Base case: if n is less than 2, simply return n (this handles the first two Fibonacci numbers: 0 and 1)
    if n < 2:
        return n

    # Initialize the first two Fibonacci numbers
    fibo_0 = 0  # F(0)
    fibo_1 = 1  # F(1)

    # Loop to calculate the nth Fibonacci number
    for _ in range(1, n):
        # Calculate the next Fibonacci number by adding the previous two
        s = fibo_0 + fibo_1
        # Move the window forward: set fibo_0 to fibo_1 and fibo_1 to the new sum
        fibo_0 = fibo_1
        fibo_1 = s

    # Return the nth Fibonacci number (fibo_0 + fibo_1 will give the last two numbers in the sequence)
    return fibo_0 + fibo_1
