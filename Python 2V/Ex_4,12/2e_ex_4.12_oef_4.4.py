import turtle
from swampy import TurtleWorld
from swampy import *
from turtle import  Turtle

# Maak een nieuw TurtleWorld-object
world = TurtleWorld

# Maak een turtle aan
bob = turtle.Turtle()
bob.delay = 0.01
bob.busy = False

# Functie om de turtle naar een positie te teleporteren
def teleport(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Functie die wordt aangeroepen bij het indrukken van een toets
def keypress(event):
    if bob.busy:
        return
    bob.busy = True

    if event.char in ['\n', '\r']:
        teleport(bob, -180, bob.ycor() - size * 3)
        bob.busy = False
        return

    func_name = 'draw_' + event.char
    func = globals().get(func_name)

    if func:
        func(bob, size)
    else:
        print("I don't know how to draw an", event.char)

    bob.busy = False

# Hier kun je jouw draw-functies definiëren, bijvoorbeeld:
def draw_a(t, size):
    # Voeg jouw tekenlogica voor 'a' toe
    pass

# Stel de grootte in
size = 20

# Teleport de turtle naar een startpositie
teleport(bob, -180, 150)

# koppel de keypress-functie aan het world
world.bind= ('<Key>', keypress)

# Start de mainloop
#world.mainloop()
