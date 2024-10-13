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
    arc_length = 2 * pi * radius * angle / 360
    detail = 30
    length_piece = arc_length / detail
    step_angle = angle / detail
    polyline(detail, length_piece, step_angle)

def arc_fixed_length(detail, length, angle):
    step_length = length / detail
    step_angle = angle / detail
    polyline(detail, step_length, step_angle)

def flower_2 (detail, length, parts):
    for _ in range (parts):
        for _ in range (2):
            arc_fixed_length(detail, length, angle = 360/parts) # * parts/2 compensates for the smaller portions
            bob.left(180 - 360/parts)
        bob.left(360 / parts)

#flower_2(30, 100, 8)
#sleep(5)


def flower (length, parts):
    for _ in range (parts):
        for _ in range (2):
            arc(radius = length, angle = 90)
            bob.left (90)
        bob.left(360/parts)
flower(100, 8)
sleep (6)
