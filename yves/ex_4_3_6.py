import turtle

from syntra_arc import arc
from syntra_polygon import polygon

radius = 100
# Do not touch the code below


def circle(t, r):
    arc(t, r, 360)


def square(t, l):
    polygon(t, l, 4)


if __name__ == "__main__":
    bob = turtle.Turtle()

    arc(bob, radius, 90)

    turtle.mainloop()
