#raised erros opzoeken

def fac(n: int) -> int:   # def fac(n: int | float) -> pipeline symbool
    if type(n) != int:
        if type(n) != float:
            raise TypeError("fac() only accepts integer arguments")


    if n < 0:
        raise ValueError("fac() only accepts positive integers")


    return 1 if n < 2 else n * fac(n - 1)



assert fac(0) == 1
assert fac(1) == 1
assert fac(2) == 2
assert fac(3) == 6
assert fac(4) == 24
assert fac(5) == 120


#-----------------## RAISE ERRORS ##-----------------#

# Om negatieve integers te testen (To test negative integers)
failed = False  # Initialize a flag to check if an error occurs
try:
    _ = fac(-1)  # Try calling the fac function with a negative number
except ValueError:  #If a ValueError occurs, it means the function correctly handles negative inputs
    failed = True  # Set the flag to True indicating the exception occurred

# Bevestig dat de exceptie heeft plaatsgevonden (Assert that the exception occurred)
assert failed, "Negative factorial should raise a ValueError"  # Als 'failed' False is, is er geen exceptie opgetreden en moet de test mislukken (If 'failed' is False, no exception occurred, and the test should fail)

#------------------------------------------------------------------------------------------------------------

# Om na te gaan of het een integer is en geen string (To check if the input is an integer and not a string)
failed = False  # Reinitialize the flag
try:
    _ = fac("a")  # ry calling the fac function with a string
except TypeError:  # If a TypeError occurs, it means the function correctly handles invalid types
    failed = True  # Set the flag to True

# Check if the fac function works for floats that represent whole numbers
assert fac(2.0) == 2  # The factorial of 2.0 should be 2 since 2.0 is equal to the integer 2
# Assert that the error occurred for passing a string
assert failed, "Only integers or whole floats are valid factorial arguments"

#------------------------------------------------------------------------------------------------------------

# To check if number-like strings are invalid
failed = False  # Reinitialize the flag again
try:
    _ = fac("2.0")  # Try calling the fac function with a string that looks like a float
except TypeError:  # If a TypeError occurs, it means strings are not accepted
    failed = True  # Set the flag to True indicating the exception occurred

# Assert that the exception occurred
assert failed, "Only integers are valid factorial arguments"  # Strings like "2.0" should raise an error


