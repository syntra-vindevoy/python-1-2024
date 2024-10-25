import math

def is_prime_optimize2(number):
    """
    This version avoids using the square root function by iterating and checking divisibility for odd numbers until the square of i exceeds number.
    Args:
        number:

    Returns:
        bool
    """
    if number < 2:
        return False
    if number == 2:
        return True  # 2 is the only even prime number
    if number % 2 == 0:
        return False  # other even numbers are not prime

    # Find the largest integer whose square is less than or equal to the number
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2  # check odd numbers only
    return True

def is_prime(number):
    """
    Args:
        number: The integer to be checked for primality.

    Returns:
        bool: True if the number is a prime number, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_prime_optimize(number):
    if number < 2:
        return False
    if number == 2:
        return True  # 2 is the only even prime number
    if number % 2 == 0:
        return False  # other even numbers are not prime
    for i in range(3, int(math.sqrt(number)) + 1, 2):  # check odd divisors only
        if number % i == 0:
            return False
    return True

assert is_prime(2) == True
assert is_prime(1) == False
assert is_prime(10) == False
assert is_prime(11) == True

assert is_prime_optimize(2) == True
assert is_prime_optimize(1) == False
assert is_prime_optimize(10) == False
assert is_prime_optimize(11) == True

assert is_prime_optimize2(2) == True
assert is_prime_optimize2(1) == False
assert is_prime_optimize2(10) == False
assert is_prime_optimize2(11) == True