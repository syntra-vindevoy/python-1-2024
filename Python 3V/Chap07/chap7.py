#Beter manier om te programmeren.


name = "Yves"
print("y" in name)

name = name.lower()
print(name)


result = "N"
# Nooit doen
if result == "Y" or result == "y":
    pass

#Wel doen
if result.upper() == "Y":
    pass

# Square roots
def newton_sqrt(n, tolerance=1e-10):
    # Starting guess
    x = n
    while True:
        # Update guess using Newton's method
        root = 0.5 * (x + (n / x))
        # Check for convergence within the specified tolerance
        if abs(root - x) < tolerance:
            return root
        x = root

# Example usage
number = 4
print(f"De wortel van {number} is ongeveer {newton_sqrt(number)}")
