import turtle



def square(t):
    for i in range(4):
        bob.fd(100)
        bob.lt(90)

if __name__ == "__main__":
    bob = turtle.Turtle()
    square(bob)
    turtle.mainloop()