import math
import turtle

def start():
    bob = turtle.Turtle ()
   # print (bob)
   # bob.fd (100)
   # bob.lt (90)
   # bob.fd (100)

    for _ in range(4):
        bob.fd (100)
        bob.lt (90)



    turtle.mainloop ()
"""
The following is a series of exercises using the turtle module. They are meant to be fun, but they have a point, too. While you are working on them, think about what the point is.

The following sections have solutions to the exercises, so don’t look until you have finished (or at least tried).

Write a function called square that takes a parameter named t, which is a turtle. It should use the turtle to draw a square.
Write a function call that passes bob as an argument to square, and then run the program again.

Add another parameter, named length, to square. Modify the body so length of the sides is length, and then modify the function call to provide a second argument. Run the program again. Test your program with a range of values for length.
Make a copy of square and change the name to polygon. Add another parameter named n and modify the body so it draws an n-sided regular polygon. Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.
Write a function called circle that takes a turtle, t, and radius, r, as parameters and that draws an approximate circle by calling polygon with an appropriate length and number of sides. Test your function with a range of values of r.
Hint: figure out the circumference of the circle and make sure that length * n = circumference.

Make a more general version of circle called arc that takes an additional parameter angle, which determines what fraction of a circle to draw. angle is in units of degrees, so when angle=360, arc should draw a complete circle.
"""
def square(t:turtle,lenght:int):
    for _ in range (4):
        t.fd (lenght)
        t.lt (90)


def polygon(t:turtle,lenght:float,n):
    angle = 360/n
    for _ in range (n):
        t.fd (lenght)
        t.lt (angle)

def arc(radius:float,angle:float):
    circumference = 2 * math.pi * radius  # Calculate the circumference of the full circle
    arc_length = circumference * (angle / 360)  # Calculate the length of the arc
    steps = int (arc_length / 2)  # Number of steps for the arc (the smaller, the smoother the arc)
    step_angle = angle / steps  # The angle to turn for each step

    for _ in range (steps):
        turtle.forward (2)  # Move forward a small amount (adjust based on smoothness)
        turtle.left (step_angle)  # Turn by the step angle

def circle(tur:turtle, radius:int):
    circumference = 2 * math.pi * radius  # Circumference of the circle
    n = 50  # Number of sides; higher n gives a smoother circle
    length = circumference / n  # Length of each side
    polygon (tur, length, n)  # Draw the polygon

def pentagon(tur:turtle, length:float):
    for _ in range (5):
        tur.fd(length)
        tur.left(72)


if __name__ == '__main__':
    #start()
    t=turtle.Turtle()
    #polygon(t,100,10)
    circle(t,100)
    #arc(100, 180)
    turtle.mainloop()
