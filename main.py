import turtle

def rectangle(height, width_rec,star):
    for i in range(2):
        star.forward(width_rec)
        star.left(90)
        star.forward(height)
        star.left(90)

def main():

    star = turtle.Turtle()
    rectangle(80, 40, star)
    turtle.done()




if __name__ == '__main__':
    main()