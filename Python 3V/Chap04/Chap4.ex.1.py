# import turtle
#
# # Create a new turtle named 'leo'
# leo = turtle.Turtle()
#
# # Move leo forward by 100 units
# leo.forward(100)
#
# # Rotate leo 90 degrees to the left
# leo.left(90)
#
# # Have leo draw a square
# for _ in range(4):
#     leo.forward(100)
#     leo.left(90)
#
# # Finish up
# turtle.done()

# import turtle
#
# # Set up the screen
# screen = turtle.Screen()
#
# # Create a turtle named 'my_turtle'
# my_turtle = turtle.Turtle()
# my_turtle.speed(1)
#
# # Draw a square
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.left(90)
#
# # End the program
# turtle.mainloop()

# import turtle
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
#
# rainbow_turtle = turtle.Turtle()
#
# rainbow_turtle.speed(10)  # Increase the drawing speed
#
# # Draw a Rainbow Benzene pattern
# for i in range(36):
#     rainbow_turtle.color(colors[i % 6])  # Cycle through the color list
#     for _ in range(6):
#         rainbow_turtle.forward(100)
#         rainbow_turtle.right(60)
#     rainbow_turtle.right(10)
#
# wn.exitonclick()


# import turtle
#
# screen = turtle.Screen()
# my_turtle = turtle.Turtle()
#
# # Set the fill color to blue
# my_turtle.fillcolor("blue")
#
# # Start filling the shape
# my_turtle.begin_fill()
#
# # Draw a square
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)
#
# # End filling the shape
# my_turtle.end_fill()
#
# screen.mainloop()


# import turtle
#
# t = turtle.Turtle()
# t.shape("turtle")  # Set the turtle shape
#
# for i in range(12):
#     t.penup()
#     t.forward(100)
#     t.pendown()
#     t.stamp()  # Leave a stamp on the canvas
#     t.penup()
#     t.backward(100)
#     t.right(30)
#
# turtle.done()


import turtle
import time

# Set up the screen
wn = turtle.Screen()
wn.title("Python Turtle Animation")
wn.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")

# Define the animation loop
# def animate():
#     for i in range(360):
#         t.speed(0)  # Fastest possible drawing speed
#         t.forward(1)
#         t.right(1)
#         wn.update()  # Manually update the screen
#         time.sleep(1/60)  # Pause for 1/60th of a second
#
# # Hide the default turtle animation and set manual update
# wn.tracer(0)
#
# # Start the animation
# animate()
#
# # Keep the window open until it's clicked
# wn.exitonclick()


import turtle

a = turtle.Turtle()
a.penup()
a.setpos(-350, -300)
a.pendown()
a.speed(0)
a.pensize(3)

colors = ["red", "blue", "green", "gray", "orange", "black", "pink", "magenta", "lightblue"]


def onecycle():
    for i in range(37):

        if i % 2 == 0:
            a.pendown()
            a.forward(i // 3)

        else:
            a.penup()
            a.forward(i / 2)


for i in range(10):
    a.color(colors[i % 9])

    onecycle()
    if i % 2 == 0:
        a.left(90)
        a.fd(20)
        a.left(90)
    else:
        a.right(90)
        a.fd(20)
        a.right(90)

turtle.exitonclick()