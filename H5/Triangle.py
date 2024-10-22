def is_triangle(a, b, c):
    # Check if the sum of any two sides is greater than the third side
    if a + b > c and a + c > b and b + c > a:
        print("Yes")
    else:
        print("No")

# Example usage:
is_triangle(3, 4, 5)  # Should print "Yes"
is_triangle(1, 1, 12)  # Should print "No"
