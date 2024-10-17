def fac(n: int) -> int:
    # The function `fac` computes the factorial of a number `n`.
    # The argument `n` is expected to be an integer, and the return type is also an integer.

    if type(n) != int:
        if type(n) != float:
        # This checks if `n` is not of type integer.
        # If not, it raises a TypeError, because factorial is only defined for integers.
            raise TypeError("fac() only accepts integer or float arguments")
        if int(n) != n:
                raise TypeError("fac() only accepts float arguments that are whole numbers")

    if n < 0:
        # This checks if `n` is a negative number.
        # Since factorial is not defined for negative numbers, a ValueError is raised.
        raise ValueError("fac() only accepts positive integers")

    # Base case: If `n` is less than 2 (i.e., 0 or 1), return 1.
    # Otherwise, use recursion: `n * fac(n - 1)` to calculate the factorial.
    return 1 if n < 2 else n * fac(n - 1)

# Test cases to ensure that the `fac` function works correctly.

# Test 1: The factorial of 0 should return 1.
assert fac(0) == 1

# Test 2: The factorial of 1 should return 1.
assert fac(1) == 1

# Test 3: The factorial of 2 should return 2 (2 * 1).
assert fac(2) == 2

# Test 4: The factorial of 3 should return 6 (3 * 2 * 1).
assert fac(3) == 6

# Test 5: The factorial of 4 should return 24 (4 * 3 * 2 * 1).
assert fac(4) == 24

# Test 6: The factorial of 5 should return 120 (5 * 4 * 3 * 2 * 1).
assert fac(5) == 120

# Test case to check if a negative input raises a ValueError.
failed = False  # Variable to track if an exception was raised.
try:
    _ = fac(-1)  # Trying to call factorial with -1.
except ValueError:
    # If a ValueError is raised, set `failed` to True.
    failed = True

# Assert that the test passed, meaning the ValueError was raised for a negative number.
assert failed, "Negative factorial should raise a ValueError"

# Test case to check if a non-integer input (string) raises a TypeError.
failed = False  # Reset the flag for the next test.
try:
    _ = fac("a")  # Trying to call factorial with a string.
except TypeError:
    # If a TypeError is raised, set `failed` to True.
    failed = True

assert fac(2.0) == 2

# Assert that the test passed, meaning the TypeError was raised for a string input.
assert failed, "Only integers or whole floats are valid factorial arguments"

# Test case to check if a non-integer input (float) raises a TypeError.
failed = False  # Reset the flag for the next test.
try:
    _ = fac(2.5)  # Trying to call factorial with a float (2.5). if you change this to 2.0 it will say that the assertion is wrong
except TypeError:
    # If a TypeError is raised, set `failed` to True.
    failed = True

# Assert that the test passed, meaning the TypeError was raised for a float input.
assert failed, "Only integers are valid factorial arguments"
