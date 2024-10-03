from datetime import datetime


def triangle(char, number):
    for i in range(1, number + 1):
        print(char * i)

def triangle2(char, number):
    # Generate the lines of the triangle in a list
    lines = [char * i for i in range(1, number + 1)]
    # Join all the lines into a single string separated by newline characters and print it
    print("\n".join(lines))

n = 1000000

start = datetime.now()

for m in range(n):
    triangle2("*", 5)

end = datetime.now()

print(end - start)