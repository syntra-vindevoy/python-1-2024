from turtle import Turtle
from time import sleep

bob = Turtle()

def square(size):
    polygon(size=size, corners=4)

def pentagon(size):
    polygon(size=size, corners=5)

def circle(size):
    polygon(size=size, corners=360)


# *, verplicht om parameters named mee te geven
# hinting door de verwachte type input mee te geven (niet afgedwongen)

def polygon(*, size: int = 100, corners: int = 4):

    for i in range(corners):
        bob.forward(size)
        bob.right(360/corners)

circle(3)

sleep(5)
