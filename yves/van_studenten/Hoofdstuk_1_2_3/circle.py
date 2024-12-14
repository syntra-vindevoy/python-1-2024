import turtle
import math

t = turtle.Turtle()

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


polygon(t, 100, 16)
print(t)
turtle.mainloop()