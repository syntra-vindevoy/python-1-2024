from turtle import Turtle
from time import sleep
from math import pi, sin, radians

bob = Turtle ()
def polygon(corners, size):
    for _ in range (corners):
        bob.forward(size)
        bob.left(360/corners)

def circle (radius):
    size = (pi * radius * 2) / 300
    polygon (300, size)

def pie_rounded (size, segments):
    for _ in range (segments):
        bob.forward(size)
        bob.left (180)
        bob.forward(size)
        bob.right(180-(360 / segments))
    bob.forward(size)
    bob.left(90)
    circle(size)

pie_rounded (100,6)
sleep (5)