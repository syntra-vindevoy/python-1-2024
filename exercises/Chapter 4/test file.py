import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle object
pen = turtle.Turtle()
pen.speed(10)
pen.pensize(3)


# Function to draw the body of the car
def draw_car_body():
    pen.penup()
    pen.goto(-200, -50)  # Starting point for the car body
    pen.pendown()

    # Draw the top of the car (roof)
    pen.setheading(0)
    pen.forward(400)  # length of car body
    pen.left(90)
    pen.forward(50)  # height of roof
    pen.left(90)
    pen.forward(400)
    pen.left(90)
    pen.forward(50)

    # Draw the front windshield
    pen.penup()
    pen.goto(-150, 0)
    pen.pendown()
    pen.setheading(40)
    pen.forward(120)

    # Draw the rear windshield
    pen.penup()
    pen.goto(150, 0)
    pen.pendown()
    pen.setheading(140)
    pen.forward(120)


# Function to draw the wheels
def draw_wheel(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("black")
    pen.begin_fill()
    pen.circle(30)  # Draw the wheel (a circle)
    pen.end_fill()


# Function to draw the windows
def draw_windows():
    pen.penup()
    pen.goto(-130, 20)
    pen.pendown()
    pen.setheading(0)
    pen.forward(80)  # Front window

    pen.penup()
    pen.goto(50, 20)
    pen.pendown()
    pen.forward(80)  # Rear window


# Function to draw the spoiler
def draw_spoiler():
    pen.penup()
    pen.goto(150, 50)
    pen.pendown()
    pen.setheading(90)
    pen.forward(20)
    pen.setheading(180)
    pen.forward(40)
    pen.setheading(270)
    pen.forward(20)


# Function to draw headlights
def draw_headlights():
    pen.penup()
    pen.goto(-200, -50)
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()

    pen.penup()
    pen.goto(200, -50)
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()


# Draw the simplified GTR car
draw_car_body()  # Body of the car
draw_wheel(-150, -80)  # Rear wheel
draw_wheel(150, -80)  # Front wheel
draw_windows()  # Windows of the car
draw_spoiler()  # Rear spoiler
draw_headlights()  # Headlights

# Hide the pen and finish the drawing
pen.hideturtle()

# Keep the turtle window open
screen.mainloop()
