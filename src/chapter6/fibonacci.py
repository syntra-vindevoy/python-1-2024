def fibonacci(n):
    """
    Calculate the n-th Fibonacci number without using recursion.

    The Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.

    Parameters:
    n (int): The position in the Fibonacci sequence to calculate. Must be a non-negative integer.

    Returns:
    int: The n-th Fibonacci number.

    Example:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(10)
    55
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n<2:
        return n

    a, b = 0, 1
    for _ in range(2,n):
        a, b = b, a + b
    return a + b


def fibonacci_rec(n):
    if n<2:
        return n
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()