import turtle

def rectangle(width, height):
    # Set up the turtle
    t = turtle.Turtle()

    # Draw the rectangle
    for _ in range(2):
        t.forward(width)   # Move forward by width units
        t.right(90)        # Turn right 90 degrees
        t.forward(height)  # Move forward by height units
        t.right(90)        # Turn right 90 degrees

    # Complete the drawing
    turtle.done()

# Example usage: Draw a rectangle 80 units wide and 40 units tall
rectangle(80, 40)
