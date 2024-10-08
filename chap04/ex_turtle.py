#Turtle
import math
from time import sleep
from turtle import Turtle       #Capital = class

bob = Turtle()                  #bob = an instance of class Turtle

#If I would write length = 100, then length becomes an optional parameter
#All optional parameters are declared in the back of the function
#When using a * as first parameter, you force the usage of named parameters (you have to mention the name of the para when calling the function
def polygon(*, corners, length):
    angle = 360 / corners

    for _ in range(corners):
        bob.forward(length)
        bob.left(angle)

def square(size):
    polygon(corners = 4, length = size)

def pentagon(size):
    polygon(corners = 5, length = size)

#def circle(size):
#    polygon(corners = 720, length = size)

def circle(radius):
    circumference = 2 * math.pi * radius
    step = circumference / 30
    polygon(corners = 720, length = step)




#square()
#pentagon()
#polygon(50, 25)
circle(2)

sleep(5)
