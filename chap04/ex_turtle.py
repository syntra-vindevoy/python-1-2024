#Turtle
import math
from time import sleep
from turtle import Turtle       #Capital = class

bob = Turtle()                  #bob = an instance of class Turtle

def polygon(corners, length):
    angle = 360 / corners

    for _ in range(corners):
        bob.forward(length)
        bob.left(angle)

def square(length):
    polygon(4, length)

def pentagon(length):
    polygon(5, length)

#def circle(length):
#    polygon(720, length)

def circle(radius):
    circumference = 2 * math.pi * radius
    step = circumference / 30
    polygon(720, step)




#square()
#pentagon()
#polygon(50, 25)
circle(2)

sleep(5)
