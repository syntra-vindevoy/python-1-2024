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
print(volume)


x = 42
result = (math.cos(x) ** 2) + (math.sin(x) ** 2)
print(result)


my_result1 = math.e ** 2
my_result2 = math.pow(math.e, 2)            # why is __y: added here???
my_result3 = math.exp(2)

print(my_result1)
print(my_result2)
print(my_result3)
