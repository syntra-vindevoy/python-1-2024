def egyptian_fraction (numerator, denominator):
    """

    The Egyptian Fraction Decomposition
    The ancient Egyptians used a unique system for representing fractions, using only sums of unit fractions
    (fractions where the numerator is 1). Any fraction could be expressed as a sum of such unit fractions.
    Args:
        numerator:
        denominator:

    Returns:

    """
    result = []
    while numerator != 0:
        x = (denominator + numerator - 1) // numerator  # Ceiling division
        result.append (x)
        numerator = x * numerator - denominator
        denominator *= x
    return result


# Example
numerator = 5
denominator = 6
fractions = egyptian_fraction (numerator, denominator)
print (f"Egyptian fraction representation of {numerator}/{denominator} is: ")
print (" + ".join ([f"1/{x}" for x in fractions]))


def lattice_multiplication (num1, num2):
    """
    Lattice multiplication is an old technique for multiplying large numbers. It involves creating a grid, filling it
     with partial products, and then summing along diagonals. It was used in Europe during the Renaissance.
    Args:
        num1:
        num2:

    Returns:

    """
    # Convert numbers to strings to access digits
    num1_str, num2_str = str (num1), str (num2)
    n, m = len (num1_str), len (num2_str)

    # Initialize a matrix to store partial products
    lattice = [[0 for _ in range (m)] for _ in range (n)]

    # Fill the lattice with products of digits
    for i in range (n):
        for j in range (m):
            product = int (num1_str[i]) * int (num2_str[j])
            lattice[i][j] = (product // 10, product % 10)  # Store tens and ones separately

    # Sum along diagonals
    diagonal_sums = []
    for d in range (n + m - 1):
        diagonal_sum = 0
        for i in range (n):
            j = d - i
            if 0 <= j < m:
                diagonal_sum += lattice[i][j][1]  # Add ones place of the product
        diagonal_sums.append (diagonal_sum)

    # Adjust for carries and compute the result
    carry = 0
    result = 0
    for d in range (len (diagonal_sums)):
        diagonal_sums[d] += carry
        carry = diagonal_sums[d] // 10
        result += (diagonal_sums[d] % 10) * (10 ** d)

    return result + carry * (10 ** len (diagonal_sums))


# Example usage
num1 = 23
num2 = 45
product = lattice_multiplication (num1, num2)
print (f"The product of {num1} and {num2} using lattice multiplication is: {product}")


def babylonian_sqrt (x, tolerance=1e-10):
    """
    The Babylonian method (also known as Heron’s method) is an ancient algorithm for approximating square roots.
    It’s essentially an early form of the Newton-Raphson method.


    Args:
        x:
        tolerance:

    Returns:

    """
    guess = x / 2.0  # Initial guess
    while abs (guess * guess - x) > tolerance:
        guess = (guess + x / guess) / 2.0
    return guess


# Example usage
x = 49
sqrt_x = babylonian_sqrt (x)
print (f"The square root of {x} using the Babylonian method is approximately: {sqrt_x}")


def karatsuba (x, y):
    """
    The Karatsuba algorithm is a divide-and-conquer method to multiply two large numbers faster
     than traditional multiplication. Instead of multiplying digit-by-digit,
     it breaks the numbers down into parts and uses clever algebra to reduce the number of multiplications.
    Args:
        x:
        y:

    Returns:

    """
    if x < 10 or y < 10:  # Base case: single-digit multiplication
        return x * y

    # Calculate the size of the numbers
    n = max (len (str (x)), len (str (y)))
    half_n = n // 2

    # Split x and y
    x_high, x_low = divmod (x, 10 ** half_n)
    y_high, y_low = divmod (y, 10 ** half_n)

    # Recursively compute three products
    z0 = karatsuba (x_low, y_low)
    z1 = karatsuba ((x_low + x_high), (y_low + y_high))
    z2 = karatsuba (x_high, y_high)

    return (z2 * 10 ** (2 * half_n)) + ((z1 - z2 - z0) * 10 ** half_n) + z0


# Example usage
num1 = 1234
num2 = 5678
product = karatsuba (num1, num2)
print (f"The product of {num1} and {num2} using Karatsuba algorithm is: {product}")
