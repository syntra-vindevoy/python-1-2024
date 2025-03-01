import math
from time import sleep
from turtle import Turtle

bob = Turtle()

#for _ in range(4):

#for _ in range(4):
    #bob.forward(100)
    #bob.left(58)

None

# * voor parameters zorgt ervoor dat je deze afdwingt en deze dus verplicht zijn, dus afdwingen van named parameters,
#code is dan ook leesbaar
#dus een hint van een variabele stel je op deze manier voor parameter: int, bv corners: int en de rest er achter dus bv
#corners: int, size: int=100
def polygon(*, corners: int, size: int=100):
    #if corners is None;:
    print(type(corners))

    a:int = 2

    for _ in range(corners):
        bob.forward(size)
        bob.left(360/corners)

#def square():
    #for _ in range(4):
        #bob.fd(100)
        #bob.lt(90)

#def pentagon():
    #for _ in range(5):
        #bob.fd(100)
        #bob.lt(72)
#1 parameter named doorgegeven, moet je ze allemaal named doorgeven
#hinting dus bv corners: int, size: int=100 geeft u een hint, maar dwingt het niet af
def square(size):
    polygon(corners=4.5, size=size)
# syntax error hierdoor

def pentagon(size):
    polygon(size=size, corners=5)

def circle(size):
    polygon(size, 360)

def circle(radius):
    circumference = 2 * math.pi * radius
        step= circumference/360
        polygon(step, 360)


#square()
#pentagon(200)
#polygon()

circle(3)
circle(radius=200)
sleep(60)


