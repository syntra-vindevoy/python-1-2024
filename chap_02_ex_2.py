import math

x = 5
sum = (math.cos(x) **2 ) + (math.sin(x) **2 )
print(f"the sum is {sum}")

deviation = abs(sum - 1)

if deviation < 0.000001:
    print(f"The sum is {sum}")