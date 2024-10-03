# A rule of trigonometry says that for any value of  𝑥 ,  (cos𝑥)2+(sin𝑥)2=1 .
# Let's see if it's true for a specific value of  𝑥  like 42.
# Create a variable named x with this value. Then use math.cos and math.sin
# to compute the sine and cosine of  𝑥 , and the sum of their squared.
# The result should be close to 1.
# It might not be exactly 1 because floating-point arithmetic is not exact---it is only approximately correct.

import math

x = 42

result = math.cos(x) ** 2 + math.sin(x) ** 2
deviation = abs(result - 1)

#result = round(result, 1)

if deviation < (10 ** - 5):
    print("Het is ok")
else:
    print(f"Het is niet ok want de uitkomst is {result}")