# Part 1. The volume of a sphere with radius r is 4/3 * pi * r^3 .
import math

radius = 5
#radius is in centimeters
volume_sphere = 4 / 3 * math.pi * radius ** 3
#volume is in cubic centimeters
print(f"The volume of a sphere with radius {radius} is {volume_sphere}")

# Part 2
x = 5
result = math.cos(x) ** 2 + math.sin(x) ** 2
deviation = abs(result - 1)

if deviation < 10 ** - 5:
    #ipv komma getallen te gebruiken: 10 ** -5 (aantal nullen na de komma)
    print(f"This is OK because the result is {result}")
else:
    print(f"This is NOT OK because the result is {result}")


# Part 3
e = math.e
print(e ** 2)
print(math.pow(e , 2))
print(math.exp(2))