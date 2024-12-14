import turtle

length = 100
corners = 4

# Do not touch the code below


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

    polygon(bob, length, corners)

    turtle.mainloop()
