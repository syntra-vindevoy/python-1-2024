import math
from time import sleep
from turtle import Turtle

bob = Turtle()

# type hinting opzoeken
# * zorgt ervoor dat alle parameters erna named moeten zijn
# corners: int is een hint parameter
def polygon(*,corners: int, size:int = 100):

# variable die gehint is
a:int = 2

    for _ in range(int(corners)):
        bob.forward(size)
        bob.left(360/corners)

# corners=4 is een named parameter
def square(size):
    polygon(corners=4, size=size)

def pentagon(size):
    polygon(size=size, corners=5)

def circle(radius):
    circumference = 2 * math.pi * radius
    step = circumference / 720
    polygon(corners=step, size=720)

#square(100)
#pentagon(100)
circle(radius=200)
sleep(60)
