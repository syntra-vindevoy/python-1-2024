#draw grid the wrong way

def rectangle():

    for i in range(1,12):
        if i == 1 or i == 6 or i == 11:
            print("+----+----+")
        else:
            print("|"," " * 2, "|", " " * 2, "|")

print(rectangle())

#-----------------------------------------------------------------------------------------------------------------------
#draw fixed grid

def rectangle2():

    for i in range(1,3):
        print("+----+----+")
        for j in range(1,5):
            print("|"," " * 2, "|", " " * 2, "|")
    print("+----+----+")

print(rectangle2())

#-----------------------------------------------------------------------------------------------------------------------
#draw grid with parameters

def rectangle3(grid_size, box_width, box_height):

    for i in range(1, grid_size + 1):
        print(("+" + "-" * box_width) * grid_size +"+")

        for j in range(1, box_height):
            print(("|" + ' ' * box_width) * grid_size + "|")

    print(("+" + "-" * box_width) * grid_size +"+")

print(rectangle3(5, 15, 6))