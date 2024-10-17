import turtle


# Function to draw a Koch curve
def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)


# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Koch Curve")

# Create the turtle
koch = turtle.Turtle()
koch.speed(0)  # Set the speed to maximum
koch.color("blue")

# Initial length of each segment and order of recursion
length = 300
order = 3

# Position the turtle
koch.penup()
koch.goto(-length / 2, 0)
koch.pendown()

# Draw the Koch curve
koch_curve(koch, order, length)

# Hide the turtle and complete
koch.hideturtle()

# Main loop to keep the window open
wn.mainloop()


