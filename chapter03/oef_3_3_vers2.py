def print_total(func1, func2, func3, nbr):
    func1(func2, func3, nbr)
    func1(func2, func3, nbr)
    func2(nbr)

def print_twice(func1, func2, nbr):
    func1(nbr)
    func2()

def first_line(nbr):
    first_line = "+ " + "- " * nbr + "+ " + "- " * nbr + "+"
    print(first_line)

def second_line():
    second_line = "|" + " " * 9 + "|" + " " * 9 + "|"
    for i in range(4):
        print(second_line)

print_total(print_twice, first_line, second_line, 4)

#def grid():
    #first_line = "+ " + "- " * 4 + "+ " + "- " * 4 + "+"
    #second_line = "|" + " " * 9 + "|" + " " * 9 + "|"

    #print(first_line)
    #for i in range(4):
        #print(second_line)

#first_line = "+ " + "- " * 4 + "+ " + "- " * 4 + "+"


#print(first_line)

    #for i in range(4):
        #print(second_line)

    #print(first_line)

  #  return first_line + "\n" + second_line

#print(grid())




