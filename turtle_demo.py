from turtle import Turtle
from time import sleep

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

def polygon(*,corners: int, size: int=100 ):
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

def circle(radius):
    circumference=2*3.14*radius
    step=circumference/720
    polygon(size=step, corners=720)

# def circle(size):
#     polygon(size=size, corners=360)



pentagon(200)
square(200)
circle(10)
sleep(10)