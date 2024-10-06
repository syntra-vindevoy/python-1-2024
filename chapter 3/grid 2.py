
def horizontal_line(size, horizontal):
    hor = ("+ " + size * "- ") * horizontal + "+"
    return hor

def vertical_line(size, horizontal):
    ver = ("| " + size * "  ") * horizontal + "|"
    return ver

def grid (size, horizontal, vertical):
    for _ in range (1, vertical+1):
        print (horizontal_line(size, horizontal))
        for _ in range (1 , size+1):
            print (vertical_line(size, horizontal))
    print (horizontal_line(size, horizontal))

grid(3,3,2)
