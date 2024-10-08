from turtle_demo import Turtle


def divide(a , b):
    return a / b

#positioneel parameters doorgeven - 1ste paramater blijft 1ste in uw functie, 2e parameter blijft 2e
# eerste parameter blijft aan a toegewezen, 2e aan b
print(divide(5,2))
# print(divide(2 , 5))

#naimed parameters - parameter doorgeven + "=" en waarde erbij
print(divide(a=6, b=2))
print(divide(b=2, a=6))

#hint naar variabele - na variabele naam ":" + spatie (leesbaarheid) & type van de variabele die je verwacht: int, float, class, ...
#type callable voor functies OF  any = kies maar, maakt niet uit
# def polygon(*, corners: int, size: int=100):
