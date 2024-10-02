import math
from turtle import penup, forward, pendown, left, right


from chapter4 import jupyturtle

jupyturtle.make_turtle ()


def jump (length):
    """Move forward length units without leaving a trail.

    Postcondition: Leaves the pen down.
    """
    penup ()
    forward (length)
    pendown ()


def inner_draw(lenght):
    forward (lenght)
    left (90)

def inner_draw_rhombus(lenght,angle):
    forward (lenght)
    left (angle)

"""
Write a function called rectangle that draws a rectangle with given side lengths. For example, here's a rectangle that's 80 units wide and 40 units tall.
"""
def rectangle (base, height):
    for _ in range (2):
        inner_draw (base)
        inner_draw (height)


def rhombus(base, angle):
    inner_angle=180-angle
    for _ in range (2):
        inner_draw_rhombus (base,angle)
        inner_draw_rhombus (base,inner_angle)


"""
Now write a more general function called parallelogram that draws a quadrilateral with parallel sides. Then rewrite rectangle and rhombus to use parallelogram"""


def parallelogram (base, height, angle):
    for _ in range (2):  # Draw two pairs of sides
        forward (base)  # Draw the first parallel side
        left (angle)  # Turn by the specified angle
        forward (height)  # Draw the second parallel side
        left (180 - angle)  # Turn to prepare for the next side

def rectangle_par (base, height):
    parallelogram (base,height,90)
def rhombus_par (base, angle):
    parallelogram (base, base,angle)

def triangle (base):
    for _ in range (3):
        forward (base)
        left (120)

def triangle_pie(radius, angle):
    """Draws one triangular segment."""
    forward(radius)  # Move the turtle forward to the circle edge
    left(180 - angle / 2)  # Turn left to draw the other sides of the triangle
    forward(2 * radius * math.sin(math.radians(angle / 2)))  # Draw the base of the triangle (chord length)
    left(180 - angle / 2)
    forward(radius)  # Complete the triangle
    left(180)  # Turn to face the original direction

def draw_pie(radius, n):
    """Draws a pie with n triangular segments."""
    angle = 360 / n  # Calculate the angle for each segment
    for _ in range(n):
        triangle_pie(radius, angle)
        right(angle)  # Turn to position for the next triangle


def main ():
    jump (-400)
    draw_pie (100, 6)
    jump (100)
    rectangle (80, 40)
    jump(100)
    rhombus(50, 60)
    jump (100)
    parallelogram (80, 50, 60)
    jump (150)
    rectangle_par (80, 40)
    jump (150)
    rhombus_par(50, 60)
    jump(100)
    triangle(80)

if __name__ == '__main__':
    main()