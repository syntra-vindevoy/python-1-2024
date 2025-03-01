import math

x = 42

y = (math.cos(x) ** 2) + (math.sin(x) ** 2)
deviation = abs(result -1)

if deviation < (10 ** -5)
    print("het is ok")
else:
    print(f"het is not want de uitkomst is {result}")


