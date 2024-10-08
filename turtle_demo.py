import math
from turtle import Turtle
from time import sleep


bob = Turtle()

#generalisatie: 1 alround function to use in later defines for functions
def polygon(size , corners):
    for _ in range(corners):
        bob.forward(size)
        bob.left(360 / corners)

def square(size):
    polygon(size ,4)

def pentagon(size):
    polygon(size , 5)

def octagon(size):
    polygon(size ,8)

def circle(radius):
    circumference = 2 * math.pi * radius
    steps = circumference / 720
    polygon(steps , 720)

# pentagon(200)
pentagon(50)
# pentagon(100)
# pentagon(75)
#circle(10)
#octagon(20)

sleep(10)

