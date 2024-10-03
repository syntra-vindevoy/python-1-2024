
def triangle(char, number):
    for i in range(number):
        print(char * (i + 1))

print(triangle("*", 5))


def triangle(char, number):
    for i in range(1, number + 1):
        print(char * i)

print(triangle("*", 5))