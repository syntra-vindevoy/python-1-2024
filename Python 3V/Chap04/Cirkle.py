import math
from turtle import Turtle
from time import sleep

bob = Turtle()

def polygon(*, corners: int, size: int=100):
    print(type(corners))

    a:int = 2

    for corn in range (int(corners)):
        bob.fd(size)
        bob.lt(360/corners)

def circle (size, corners):
    radius = size / 2
    circumference = 2 * math.pi * radius
    step = circumference / corners
    polygon(corners= corners, size=step)

#square()
#pentagon(200)
#polygon(corners=5)
circle(200,720)

sleep(50)
