import math

x = 5
sum = (math.cos(x) **2 ) + (math.sin(x) **2 )
print(f"the sum is {sum}")

deviation = abs(sum - 1)

if deviation < 0.000001:
    print("Het is ok")
else:
    print(f"Het is niet ok want de uitkomst is {sum}")
