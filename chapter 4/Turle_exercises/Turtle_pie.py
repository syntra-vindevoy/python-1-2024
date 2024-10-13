from turtle import Turtle
from time import sleep
from math import radians
from math import sin

bob = Turtle()

def triangle (size, angle):
    opposing_angle = (180 - angle) / 2
    other_side = 2 * size * sin(radians(angle / 2)) #calculates the other side using radians instead of degrees
    bob.forward(size)
    bob.left(180 - opposing_angle)
    bob.forward(other_side)
    bob.left(180 - opposing_angle)
    bob.forward(size)

def draw_pie(segments, size):
    for _ in range (segments):
        triangle (size, 360 / segments)
        bob.left(180)

draw_pie (10, 100)
sleep (5)




