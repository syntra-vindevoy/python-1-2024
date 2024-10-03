def grid_horizontal_line():
    print("+" , end= "")

    for i in range(columns):
        print(" -" , end= "")
    print(" +" , end= "")
    for i in range(columns):
        print(" -" , end= "")

    print(" +", end="")
    print()

def height(f):
    f()
    f()
    f()
    f()

def grid_vertical_line():
    print("/" , end="")
    print(" " * 9 , end="")
    print("/" , end="")
    print(" " * 9, end="")
    print("/")



columns = 2
rows = 2
grid_horizontal_line()


