import jupyturtle

from turtle import Turtle
from time import sleep
import math

bob = Turtle()

def polygon(size,corners):
    for i in range(corners):
        bob.forward(size)
        bob.left(360/corners)


def square(size):
    polygon(size, 4)

def pentagon(size):
    polygon(size, 5)

def circle(radius):
    circumference = 2*math.pi*radius
    step = circumference/720
    polygon(step, 720)

circle(5)

sleep(60)