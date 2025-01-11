import math

def trigo(*, x:int) -> float:
    return (math.cos(x)**2) + (math.sin(x)**2)

for i in range(1, 50, 1):
    print(trigo(x=i))