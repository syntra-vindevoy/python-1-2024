
def line_1():
    part_1 = "+ " + 4 * "- "
    return part_1
print(line_1())
def line_2():
    part_2 = f"| {(8 * " ")}"
    print (part_2 * 3)

def grid_half ():
    line_1()
    for i in range (1, 5):
        line_2()

def grid():
    grid_half()
    grid_half()
    line_1()

grid()

def edge_line():
    ou = "+" + ("-" * 4 + "+") * 5
    part = "+ " + 4 * "- "
    return ou


print (edge_line())

