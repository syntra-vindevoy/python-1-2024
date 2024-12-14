import math
import turtle

radius = 100
# Do not touch the code below


def arc(t, r, d):
    # omtrek = 2*pi*r

    n = 2 * math.pi * r

    for i in range(d):
        t.fd(n/360)
        t.lt(1)

def circle(t, r):
    # omtrek = 2*pi*r

    n = 2 * math.pi * r

    for i in range(360):
        t.fd(n/360)
        t.lt(1)


def polygon(t, l, n):
    for i in range(n):
        t.fd(l)
        t.lt(360 / n)


def square(t, l):
    for i in range(4):
        t.fd(l)
        t.lt(90)


if __name__ == "__main__":
    bob = turtle.Turtle()

    arc(bob, radius, 45)

    turtle.mainloop()
