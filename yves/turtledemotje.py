from turtle import Turtle
from time import sleep

bob = Turtle()
def polygon(size, corners):
    for _ in range(corners):
        bob.forward(2)
        bob.left(720 / corners)


def pentagon(size):
    for i in range(5):
        bob.forward(100)
        bob.left(72)

def square(size):
    polygon(size, 4)

def circle(size):
     polygon (size, 360)


circle(3)




