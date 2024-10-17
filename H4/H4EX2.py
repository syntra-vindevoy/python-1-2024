import turtle

def rhombus(side_length, angle):
    # Set up the turtle
    t = turtle.Turtle()

    # Draw the rhombus
    for _ in range(2):
        t.forward(side_length)   # Move forward by side_length units
        t.left(angle)            # Turn left by the interior angle
        t.forward(side_length)   # Move forward by side_length units
        t.left(180 - angle)      # Turn left by the supplementary angle

    # Complete the drawing
    turtle.done()

# Example usage: Draw a rhombus with side length 50 and interior angle 60 degrees
rhombus(50, 60)
