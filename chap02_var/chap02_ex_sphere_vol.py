import math

def sphere_val(*, r:int) -> int:
    vol = (4/3) * math.pi * (r**3)

    return vol

print(f"The volume of the sphere is: {sphere_val(r = 5)}")