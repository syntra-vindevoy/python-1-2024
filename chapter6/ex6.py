import math
import sys


# Use incremental development to write a function called hypot
# that returns the length of the hypotenuse of a right triangle given the lengths of the other two legs as arguments.


def hypot(a, b):

    return math.sqrt(a**2 + b**2)

# Example test cases
print(hypot(3, 4))  # Expected output: 5.0
print(hypot(0, 0))  # Expected output: 0.0
print(hypot(0, 5))  # Expected output: 5.0
print(hypot(5, 0))  # Expected output: 5.0


def is_between(x, y, z):
    if x < y < z or x > y >z:
        return True
    else:
        return False

print(is_between(1, 2, 3))
print(is_between(3, 2, 1))
print(is_between(1, 3, 1))

sys.setrecursionlimit(10000)
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(0, 0))  # Output: 1
print(ackermann(1, 2))  # Output: 4
print(ackermann(2, 2))  # Output: 7
print(ackermann(3, 2))  # Output: 29

#print(ackermann(5, 5))  # Output: 29


# A number,  a , is a power of  b  if it is divisible by  b  and  a/b  is a power of  b .
# Write a function called is_power that takes parameters a and b and returns True if a is a power of b.
# Note: you will have to think about the base case.
def is_power(a, b):
    # Base case: if a equals 1, it's a power of any number.
    if a == 1:
        return True
    # If b equals 1, a can only be 1 to be considered a power of b.
    if b == 1:
        return a == 1
    # Recursive case: a must be divisible by b and a/b should be a power of b.
    if a % b == 0:
        return is_power(a // b, b)
    else:
        return False

# Example usage:
print(is_power(8, 2))   # True (2^3 = 8)
print(is_power(27, 3))  # True (3^3 = 27)
print(is_power(16, 4))  # False (no power of 4 equals 16)
print(is_power(1, 5))   # True (5^0 = 1)
print(is_power(9, 3))   # True (3^2 = 9)
print(is_power(15, 3))  # False (no power of 3 equals 15)

# The greatest common divisor (GCD) of  a  and  b  is the largest number that divides both of them with no remainder.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example usage:
print(gcd(48, 18))  # Output: 6
print(gcd(54, 24))  # Output: 6
print(gcd(17, 13))  # Output: 1 (since 17 and 13 are co-prime)
