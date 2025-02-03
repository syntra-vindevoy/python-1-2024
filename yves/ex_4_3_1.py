import turtle

bob = turtle.Turtle()


def square(length):
    for i in range(4):
        bob.fd(length)
        bob.lt(90)


if __name__ == "__main__":
    square(100)

    turtle.mainloop()
