from time import sleep
from turtle import Turtle

bob = Turtle()

# een vierkant tekenen met de turtle functie
#bob.forward(100)
#bob.left(90)
#bob.forward(100)
#bob.left(90)
#bob.forward(100)
#bob.left(90)
#bob.forward(100)

#defenitie voor een veelhoek
def polygon(size, corners):
    for _ in range(corners):
        bob.forward(size)
        bob.left(360 / corners)

# onderstaande tekent hetzelfde vierkant, maar dan met for lus
def square():
    for _ in range(4):
        bob.forward(100)
        bob.left(90)

# polygon is niet echt sexy en zal niet veel gebruikt worden
# daarom kunnen we bovenstaande Square functie wel nog gebruiken, en gewoon polygon oproepen.
# die polygon functie gaan we in alle funties dan oproepen
# de polygon functie wordt de functie die we dan later moeten aanpassen
def square2(size):
    polygon(size, 4)

def pentagon():
    for _ in range(5):
        bob.forward(100)
        bob.left(72)

def circle(size):
    polygon (size, 360)

# circle function met een radius ipv size
def circle2(radius):
    circumference = radius * math.pi * 2
    step_forward = circumference / 720
    polygon(step, 720)

#square()
#pentagon()
#polygon(4, 10)

#square2(100)

circle(5)

sleep(5) #dit zorgt ervoor dat scherm in slaapstand gaat voor 10 seconden

