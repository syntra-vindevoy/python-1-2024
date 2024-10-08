import math
from time import sleep
from turtle import Turtle


bob = Turtle()

def polygon(*, corners: int, size:int = 100):
    print(type(corners))

    a:int = 2.0

    for _ in range(corners):
        bob.forward(size)
        bob.left(360/corners)




def square(size):
    polygon(corners=4, size=size)

def pentagon(size):
    polygon(size=size, corners=5)

def circle(radius):
    circumference = 2 * math.pi * radius
    step = circumference / 720
    polygon(corners=step, size=720)

square(100)
#pentagon(200)
#polygon(4)

#circle(radius=200)
sleep(60)