import math
from turtle import Turtle
from time import sleep

bob = Turtle()

def polygon(*, corners: int, size: int = 100):
    for _ in range(int(corners)):
        bob.forward(size)
        bob.left(360 / corners)

def square(size):
    polygon(corners=4, size=size)

square(size=100)
sleep(10)