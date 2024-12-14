from turtle import *


def snowflake(length_side, levels):
    if levels == 0:
        forward(length_side)
        return
    length_side /= 3.0
    snowflake(length_side, levels - 1)
    left(60)
    snowflake(length_side, levels - 1)
    right(120)
    snowflake(length_side, levels - 1)
    left(60)
    snowflake(length_side, levels - 1)



if __name__ == "__main__":

    speed(0)
    length = 300.0
    penup()
    backward(length / 2.0)
    pendown()
    for i in range(3):
        snowflake(length, 4)
        right(120)


    mainloop()