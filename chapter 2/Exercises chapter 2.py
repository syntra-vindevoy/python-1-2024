import math

radius = 5 #centimeters
volume = 4 / 3 * math.pi * (radius ** 3) #result in cubic centimeters
print (f"the volume of the sphere with a {radius} cm radius is {volume} cm³")

x = 42
close_to_1 = (math.cos(x)) ** 2 + (math.sin(x)) ** 2
print (close_to_1)
deviation = abs(close_to_1 - 1)
if deviation < 0.00000001:
    print("het is oke")
if deviation <10**-5:
    print("dit is ook oke")
print (math.e **2)
resultaat = math.pow(math.e,2)
print (resultaat)
print (math.pow(math.e,2))
print (math.exp(2))

print (float(10**-8))
