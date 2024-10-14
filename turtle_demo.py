from turtle import Turtle
from time import sleep
import math
import turtle as t

bob=Turtle()


# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# * verplicht u de parameters named te maken...
# size=100 ==> is in het geval size niet wordt meegeven...
# int achter parameters = definieer waarde. Dit is hinting wat wil zeggen
# dat het ookal is het een float in het programma het gaat werken. Het wordt niet afgedwongen.

def polygon(*,corners: int, size: int=100):
    for _ in range(corners):
        bob.forward(size)
        bob.left(360/corners)


def square(size):
    # for _ in range(50):
    #     bob.forward(100)
    #     bob.left(90)
    polygon(size=size, corners=4)

def pentagon(size):
    # for _ in range(5):
    #     bob.forward(100)
    #     bob.left(72)
    polygon(size=size, corners=5)

def triangle(size, corners2=9):
    for _ in range(corners2):
        polygon(size=size, corners=3)
        bob.right(360 / corners2*2)

def circle(radius):
    circumference=2*3.14*radius
    step=circumference/720
    polygon(size=step, corners=360)




def rhombus(side_length, angle):
    # Calculate internal angles
    angle_rad = math.radians(angle)
    other_angle = 180 - angle

    # Setting up the turtle
    bob.speed(1)  # Set the speed to 1 for visualization, can use 0 for fastest

    for _ in range(2):
        bob.forward(side_length)
        bob.left(angle)
        bob.forward(side_length)
        bob.left(other_angle)

    turtle.done()




# Example usage:
rhombus(100, 60)

triangle(100)
#pentagon(200)
#square(200)
#circle(100)
sleep(10)

