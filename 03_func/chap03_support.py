#Support program to 03_func

def add(x, y):
    a = x + y

    #print(a)
    return a

def div(x, y):
    a = x / y
    return a


assert add(2, 3) == 5          #will generate an error when you'd make a mistake in your function for example * instead of +

def __main__():                      #Good practice!!!
    print(add(2 , 3))


if __name__ == '__main__':          #only run this code when you're really running the file
    __main__()                      #Good practice!!!
