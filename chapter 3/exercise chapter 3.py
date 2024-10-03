def print_right (text):
    print(f"{(40 -len(text)) * ' '}{text}")

print_right ("hallo")
print_right ("hey")

def main():
    print_right ("a")
    print_right ("b")
    print_right ("c")

if __name__ == '__main__':
    main()

def print_right (text):
    text.strip()
    assert len(text) <= 40
    return f"{(40 -len(text)) * ' '}{text}"
print (print_right ("ABC"))


def triangle (char , number):
    for i in range(1 , number+1):
        print(char * i)

triangle ("L", 5)
triangle ("S", 10)


def rectangle( char, width, height):
    for i in range(1 , height+1):
        print(char * width)
rectangle ("X", 5 , 8)

def do_twice (f):
    f()
    f()
do_twice (rectangle("E", 3 , 4 ))

part_1 = "+ " + "- "
def line_1():
    print (part_1 * 2) + "+"

line_1()
print ("jhkjhj")

print (f"hallo", end="")
print ("wazaa")

def nog_niet_af():
    pass
 for _ in range (8): #_geeft geen fout als nog niet toegekend

