import math
from turtle import Turtle

bob = Turtle()


def polygon(corners: int, size: int = 100):
    for _ in range(corners):
        bob.forward(size)
        bob.left(360 / corners)


def square(size: int):
    polygon(corners=4, size=size)


def pentagon(size: int):
    polygon(corners=5, size=size)


def circle(radius: int):
    circumference = 2 * math.pi * radius
    step = circumference / 720
    for _ in range(int(circumference / step)):
        bob.forward(step)
        bob.left(360 / circumference)


# Example usage
square(100)
pentagon(100)
circle(100)