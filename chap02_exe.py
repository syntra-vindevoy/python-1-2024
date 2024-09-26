###Exercise 2.11.2###
# 1: 17 = n --> syntax error

# 2: x = y = 1 --> yes you can assign variables like this

# 3: ; --> has no effect on the code, however it can be used to put multiple statements on when line (not recommended)
x = 10; y = 20; z = x + y
print(z)

# 4: putting a period at the end of a statement gives a syntax error

# 5: Writing the name of a module wrong will result in an error

###Exercise 2.11.3###
import math

radius = 5                                  #radius in cm
volume = (4/3) * math.pi * (radius ** 3)    #volume in cm²
print(f"The volume of the sphere with radius {radius} is: {volume}")


x = 5
result = (math.cos(x) ** 2) + (math.sin(x) ** 2)
dev = abs(result - 1)

if dev < (10 ** -5):
    print("The statement is TRUE")
else:
    print("The statement is FALSE")

print(f"The result of cos({x})² + sin({x})² is {round(result)}")


my_result1 = math.e ** 2
my_result2 = math.pow(math.e, 2)            # why is __y: added here???
my_result3 = math.exp(2)

print(f"The result of e² with method 1 is {my_result1}")
print(f"The result of e² with method 2 is {my_result2}")
print(f"The result of e² with method 3 is {my_result3}")
