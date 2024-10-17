import turtle

# Create the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Duvel Beer Bottle")

# Create the turtle
duvel_bottle = turtle.Turtle()
duvel_bottle.color("brown")
duvel_bottle.pensize(3)


# Function to draw the Duvel beer bottle
def draw_duvel_bottle():
    duvel_bottle.penup()
    duvel_bottle.goto(-50, -200)
    duvel_bottle.pendown()

    # Bottle base
    duvel_bottle.begin_fill()
    duvel_bottle.circle(50, 180)  # left half of the bottom circle
    duvel_bottle.left(90)
    duvel_bottle.forward(100)  # right side of the bottle
    duvel_bottle.left(85)
    duvel_bottle.forward(50)  # transition to the neck
    duvel_bottle.left(95)
    duvel_bottle.forward(40)  # narrow neck
    duvel_bottle.circle(10, 180)  # top of the neck
    duvel_bottle.forward(40)  # narrow neck
    duvel_bottle.left(95)
    duvel_bottle.forward(50)  # transition to body
    duvel_bottle.left(85)
    duvel_bottle.forward(100)  # left side of the bottle
    duvel_bottle.left(90)
    duvel_bottle.circle(50, 180)  # right half of the bottom circle
    duvel_bottle.end_fill()

    # Bottle cap
    duvel_bottle.penup()
    duvel_bottle.goto(-10, 40)
    duvel_bottle.pendown()

    duvel_bottle.color("gray")
    duvel_bottle.begin_fill()
    duvel_bottle.right(95)
    duvel_bottle.forward(35)  # cap width
    duvel_bottle.left(95)
    duvel_bottle.forward(10)  # cap height
    duvel_bottle.left(85)
    duvel_bottle.forward(35)  # cap width
    duvel_bottle.left(90)
    duvel_bottle.forward(10)  # cap height
    duvel_bottle.end_fill()

    # Draw label for extra detail
    duvel_bottle.penup()
    duvel_bottle.goto(-40, -50)
    duvel_bottle.color("white")
    duvel_bottle.pendown()
    duvel_bottle.begin_fill()
    duvel_bottle.forward(80)
    duvel_bottle.left(90)
    duvel_bottle.forward(30)
    duvel_bottle.left(90)
    duvel_bottle.forward(80)
    duvel_bottle.left(90)
    duvel_bottle.forward(30)
    duvel_bottle.end_fill()

    # Optional: add text to the label
    duvel_bottle.penup()
    duvel_bottle.goto(-30, -40)
    duvel_bottle.color("red")
    duvel_bottle.write("Duvel", move=False, align="center", font=("Arial", 16, "bold"))


# Call the function to draw the Duvel beer bottle
draw_duvel_bottle()

# Hide the turtle and complete
duvel_bottle.hideturtle()

# Main loop to keep the window open
wn.mainloop()
