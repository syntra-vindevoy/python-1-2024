from turtle import Turtle
theo = Turtle()

def rectangle(wide, tall):
    for i in range(2):
        theo.forward(wide)
        theo.left(90)
        theo.forward(tall)
        theo.left(90)

#rectangle(80, 40)

def rhombus(length, angle):
    theo.forward(length)
    theo.left(angle)
    theo.forward(length)
    theo.left(90+90-angle)
    theo.forward(length)
    theo.left(angle)
    theo.forward(length)

#rhombus(50, 60)
def rhombus2(length2, angle2):
    for i in range(2):
        theo.forward(length2)
        if i := 1:
            angle2 = (90 + 90 - angle2)
            theo.forward(length2)

        theo.left(angle2)

rhombus2(50, 60)