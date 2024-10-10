# Optie 1
# from time import sleep
# from turtle import Turtle
#
# bob = Turtle()
#
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
#
# sleep(60)
#import math
# # Optie 2
# from time import sleep
# from turtle import Turtle
#
# bob = Turtle()
#
# for i in range(4):
#     bob.forward(100)
#     bob.left(90)
#
# sleep(2)

# Optie 2 Youssef
import  math
from time import sleep
from turtle import Turtle

from Chap2_Type import radius

bob = Turtle()

def polygon(*, corners: int, size: int=100):
    print(type(corners))

    a:int = 2

    for corn in range (int(corners)):
        bob.fd(size)
        bob.lt(360/corners)

def square(size):
    polygon(corners= 4, size=size)
    # for i in range(4):
    # bob.fd(200)
    # bob.lt(90)

def pentagon(size, corners):
    polygon(size=size, corners=5)
    # for i in range(5):
    #     bob.forward(100)
    #     bob.left(72)

def circle (size, corners):
    radius = size / 2
    circumference = 2 * math.pi * radius
    step = circumference / corners
    polygon(corners= corners, size=step)

#square()
#pentagon(200)
#polygon(corners=5)
circle(200,720)

sleep(50)


#Voorbeeld Yves
# import math
# from time import sleep
# from turtle import Turtle
#
#
# bob = Turtle()
#
# def polygon(*, corners: int, size:int = 100):
#     print(type(corners))
#
#     a:int = 2.0
#
#     for _ in range(corners):
#         bob.forward(size)
#         bob.left(360/corners)
#
#
#
#
# def square(size):
#     polygon(corners=4, size=size)
#
# def pentagon(size):
#     polygon(size=size, corners=5)
#
# def circle(radius):
#     circumference = 2 * math.pi * radius
#     step = circumference / 720
#     polygon(corners=step, size=720)
#
# square(100)
# #pentagon(200)
# #polygon(4)
#
# #circle(radius=200)
# sleep(60)