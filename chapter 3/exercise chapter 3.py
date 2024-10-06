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

def kerstboom (char, size):
    for i in range (size+1, 1, -1):
        print (" " * i + char*(size+2 -i) + char * (size+1-i))
    print (" " * (size+1) + "|")
kerstboom ("x", 7)
