import math

x = 5

result = math.cos(x) ** 2 + math.sin(x) ** 2
deviation = abs(result - 1)

if deviation < (10 ** -5):
    print("het is ok")
else:
    print(f"het is niet ok want de uitkomst is {result}")
