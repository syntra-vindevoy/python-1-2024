import math

x = 42
val_cos = math.cos(x) ** 2
val_sin = math.sin(x) ** 2
val_sum = val_cos + val_sin
print(f"the cos of {x} is {val_cos} and the sin of {x} is {val_sin}, the sum of both is {val_sum}")

#alternative solution 2_2

import math

x = 5

result = math.cos(x) **2 + math.sin(x) ** 2
deviation = abs(result - 1)

if deviation < 10 ** -5:
    print("het is ok")
else:
    print(f"het is niet ok want de uitkomst is {result}")
