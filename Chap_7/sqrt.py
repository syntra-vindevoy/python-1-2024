# Define a custom square root function using Newton's method
def mysqrt(a, tolerance=1e-10):
    # Initial guess
    x = a
    while True:
        # Update guess
        y = (x + a / x) / 2
        # Check for convergence
        if abs(y - x) < tolerance:
            return y
        x = y