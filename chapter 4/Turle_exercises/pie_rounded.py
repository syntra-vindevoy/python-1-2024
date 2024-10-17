from turtle import Turtle
from time import sleep
from math import pi, sin, radians

bob = Turtle ()
def polygon(corners, size):
    for _ in range (corners):
        bob.forward(size)
        bob.left(360/corners)

def circle (radius, detail):
    size = (pi * radius * 2) / detail
    polygon (detail, size)

def polyline(n, length, angle):
    for i in range(n):
        bob.forward(length)
        bob.left(angle)

def pie_rounded (size, segments, detail):
    for _ in range (segments):
        bob.forward(size)
        bob.left (180)
        bob.forward(size)
        bob.right(180-(360 / segments))
    bob.forward(size)
    bob.left(90)
    circle(size, detail)

#pie_rounded (100,6, 50)
#sleep (5)

def arc(radius, angle):
    #calculates an arc piece and divides it into smaller pieces to it draw using polyline function
    arc_length = 2 * pi * radius * angle / 360
    detail = 30
    length_piece = arc_length / detail
    step_angle = angle / detail
    polyline(detail, length_piece, step_angle)

def pie_rounded_alt (size, segments, detail):
    for _ in range (segments):
        bob.forward(size)
        bob.left(90)
        arc (size , 360 / segments)
        bob.left(90)
        bob.forward(size)
        bob.left(180)
pie_rounded_alt (100, 5, 30)