import math


def my_sqrt(a: float):
    x=3
    while True:
        y = (x + a/x) / 2
        if y == x:
            return x
        x = y
print("a  mysqrt(a) math.sqrt(a)  diff")
for i in range(1,10):
    mx:float=my_sqrt(i)
    m:float=math.sqrt(i)
    print (f"{i} {mx:.8f}    {m:.8f}     {mx - m:.8f}")


# Cardtalk puzzelers money machine
# is primegetal
# sum van 1 tot 10
# 1  11  21  1211 111221 312211


