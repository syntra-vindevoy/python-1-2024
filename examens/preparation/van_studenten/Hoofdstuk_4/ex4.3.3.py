import turtle


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


if __name__ = "__main__":
    t = turtle.Turtle()
    square(t, 400)
    print(t)
    turtle.mainloop()
