import turtle

def parallelogram(side1, side2, angle):
    # Set up the turtle
    t = turtle.Turtle()

    # Draw the parallelogram
    for _ in range(2):
        t.forward(side1)     # Move forward by side1 units
        t.left(angle)        # Turn by the given angle
        t.forward(side2)     # Move forward by side2 units
        t.left(180 - angle)  # Turn by the supplementary angle

    # Complete the drawing
    turtle.done()

def rectangle(width, height):
    # A rectangle is a special case of a parallelogram with angle = 90 degrees
    parallelogram(width, height, 90)

def rhombus(side_length, angle):
    # A rhombus is a special case of a parallelogram where all sides are equal
    parallelogram(side_length, side_length, angle)

# Draw a rectangle 80 units wide and 40 units tall
rectangle(80, 40)

# Draw a rhombus with side length 50 and an interior angle of 60 degrees
rhombus(50, 60)
