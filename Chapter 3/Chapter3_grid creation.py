def grid_horizontal_line():
    print("+", end=" ")
    print("- " * 4 , end="")
    print("+" , end=" ")
    print("- " * 4, end="")
    print("+")

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

grid_horizontal_line()
height(grid_vertical_line)
grid_horizontal_line()
height(grid_vertical_line)
grid_horizontal_line()