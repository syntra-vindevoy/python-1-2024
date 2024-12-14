import turtle



def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


if __name__ = "__main__":
    t = turtle.Turtle()
    polygon(t, 100, 16)
    print(t)
    turtle.mainloop()