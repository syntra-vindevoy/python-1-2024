import math

from winerror import HRESULT_FROM_WIN32

radius = 5

volume = (4/3) * math.pi * (radius ** 3)
print(f"The volume of the sphere is {volume} cubic centimeters.")

x = 42
result1 = math.cos(x)**2+math.sin(x)**2
print(f"The result of this calculation is {result1}.")
deviation = abs(result1 - 1)

if deviation < 0.000000000001:
    print("True")
else:
    print ("False")

y = math.e**2
z = math.exp(2)

print(f"math.e**2 is {y}.")
print(f"math.exp(2) is {z}.")

price = 24.95
discount = 0.4
ship1 = 3
ship2 = 0.75
q = 60
result = (price * (1-discount) * q) + ship1 + (ship2*(q-1))
result = round(result,2)

print (result)

easy = 2 * (8 * 60 + 15)
fast = 3 * (7 * 60 + 12)

duration_s = easy + fast

left_h = 6
left_m = 52
left_s = 0

left_ts = (left_h * 3600) + (left_m * 60) + left_s

home_ts = left_ts + duration_s

home_h = int(home_ts // 3600)
home_m= int((home_ts % 3600) // 60)
home_s = int(home_ts % 60)

print(f"{home_h:02d}:{home_m:02d}:{home_s:02d}")

from