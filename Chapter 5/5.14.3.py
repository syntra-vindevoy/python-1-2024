# Write a function named is_triangle that takes three integers as arguments,
# and that prints either “Yes” or “No”,
# depending on whether you can or cannot form a triangle from sticks with the given lengths.
# Hint: Use a chained conditional.

###

# If any of the three lengths is greater than the sum of the other two,
# then you cannot form a triangle.
# Otherwise, you can. (If the sum of two lengths equals the third, they form what is called a “degenerate” triangle.)

###

"""This function checks whether three given side lengths (a, b, c) can form a valid triangle.
It returns a boolean value: True if the sides satisfy the triangle inequality theorem, and False otherwise."""

def is_triangle(a: int, b: int, c: int) -> bool:
    if a > (b + c) or b > (c + a) or c > (a + b):
        print("No")
    else:
        print("Yes")


is_triangle(7, 2, 3)