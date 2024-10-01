#Functions
from chap03_support import add


def my_greeting():
    print("Hello")

print(type(my_greeting))
my_greeting()

def printing(text):
    print(text)

printing("Hello World")
printing(1 + 1)

def calc_area(b, h):
    return b * h

print(calc_area(5, 10))


for i in range(2):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):       #1 = start point / 2 = until (but not included) / 3 = add i with this number
    print(i)

#############################################################################
def add1(x, y):
    a = x + y                   #'a' is local just within the function

    print(a)

a = 100                         #bad practice, but this a is a completely different a than the one in the function

print(a)

add(2, 3)

print(a)

