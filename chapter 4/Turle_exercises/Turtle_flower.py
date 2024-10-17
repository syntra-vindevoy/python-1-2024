from turtle import Turtle
from time import sleep
from math import pi

bob = Turtle ()

def polygon(corners, size):
    for _ in range (corners):
        bob.forward(size)
        bob.left(360/corners)

def circle (radius):
    size = (pi * radius * 2) / 300
    polygon (300, size)

def polyline(n, length, angle):
    for i in range(n):
        bob.forward(length)
        bob.left(angle)

def arc(radius, angle):
    #calculates an arc piece and divides it into smaller pieces to it draw using polyline function
    arc_length = 2 * pi * radius * angle / 360
    detail = 30
    length_piece = arc_length / detail
    step_angle = angle / detail
    polyline(detail, length_piece, step_angle)

def arc_fixed_length(detail, length, angle):
    #divides an arc of a defined length and angle into a defined number of pieces to draw it using polyline function
    step_length = length / detail
    step_angle = angle / detail
    polyline(detail, step_length, step_angle)

def flower_2 (detail, length, parts):
    """
        Draws a flower-like pattern using arcs and rotations, dividing the pattern into specified parts.

        Parameters
        ----------
        detail : int
            The number of segments to divide each arc into.
        length : float
            The length of each arc in the pattern.
        parts : int
            The number of petals or parts in the flower pattern.

        Returns
        -------
        None
            The function doesn't return anything but uses `arc_fixed_length`
            and `bob.left()` to create the pattern.

        Notes
        -----
        - The pattern consists of `parts` number of petals.
        - Each petal is formed by two arcs, with each arc having an angle of `360 / parts` degrees.
        - After each arc, the `bob.left()` function is called to rotate and position the next petal.
        - The `arc_fixed_length` function is used to draw each arc.


        """
    for _ in range (parts):
        for _ in range (2):
            angle = 360 / parts #makes the parts getting thinner while the number of parts grow so they never overlap
            arc_fixed_length(detail, length, angle)
            bob.left(180 - 360 / parts)
        bob.left(360 / parts)

def flower (length, parts):
    """
       Draws a flower-like pattern using quarter-circle arcs and rotations, dividing the pattern into the specified number of parts.

       Parameters
       ----------
       length : float
           The radius of the arcs used to create the flower pattern.
       parts : int
           The number of petals or parts in the flower pattern.

       Returns
       -------
       None
           The function doesn't return anything but uses `arc` and `bob.left()`
           to create the pattern.

       Notes
       -----
       - Each petal consists of two quarter-circle arcs, each with a fixed angle of 90 degrees.
       - The function uses `bob.left(90)` after each arc to rotate and position the next part of the petal.
       - After creating a petal, the function calls `bob.left(360 / parts)` to position for the next petal.
       - The `arc` function is used to draw the arcs, and it requires a `radius` and an `angle`.

       """
    for _ in range (parts):
        for _ in range (2):
            arc(radius = length, angle = 90)
            bob.left (90)
        bob.left(360/parts)
#flower(100, 10)
#flower(100, 3)
#sleep(5)