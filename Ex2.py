n = 17
# 17 = n ==> syntax error
a = y = 1
z = 2;
# e = 3. syntax error
# import maath ==> syntax error

# part 1

import math

# radius is in centimeters
radius = 5

# volume in cubic centimeters
volume = (4/3) * math.pi * radius**3

print("The volume of the sphere is:", volume, "cubic centimeters")

# part 2

# Define the value of x in radians
x = 5  # x in radians

# Compute cosine and sine of x
cos_x = math.cos(x)
sin_x = math.sin(x)

# Calculate the sum of their squares
result = cos_x**2 + sin_x**2
result = round(result, 1)
deviation = abs(result -1)
# Display the result
print(f"cos^2(x) + sin^2(x) = {result}")

#om te weten als de uitkomst waar is.
if deviation < (10 ** -5):
    print("het is ok")
else :
    print(f"het is niet in orde, want de uitkomst is {result} ")


# if result == 1:
#     print("het is ok")
# else :
#     print(f"het is niet in orde, want de uitkomst is {result} ")


# part 3

# First method: Directly using math.e
e_squared_1 = math.e ** 2

# Second method: Using math.pow function
e_squared_2 = math.pow(math.e, 2)

# Third method: Using math.exp to compute e raised to the power of 2
e_squared_3 = math.exp(2)

# Display the results
print(f"result with math.e ** 2: {e_squared_1}")
print(f"result with math.pow: {e_squared_2}")
print(f"result with math.exp: {e_squared_3}")

price = 24.95
discount = 40 / 100
first_book_chip = 3
rest_book_chip = 0.75
amount_books = 10000
discount_price = price * (1 - discount)
print(discount_price)
totalcost = ((discount_price * amount_books) + (rest_book_chip * (amount_books - 1)) + first_book_chip)
rounded = round(totalcost, 2)


print(f"totale prijs om een book te kopen: ${rounded} waarvan ")


