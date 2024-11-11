# This function calculates if a triangle can be made based on a cartesian coordinate system.

def is_triangle(x1, x2, y1, y2):

    import math

    dx = abs(x2 - x1)

    dy = abs(y2 - y1)

    dz = math.sqrt(dx**2 + dy**2)

    if dz > dx + dy:
        return "No"
    elif dx > dy + dz:
        return "No"
    elif dy > dx + dz:
        return "No"
    else:
        return "Yes"

print(is_triangle(10, 10, 10, 10))

# This function calculates if a triangle can be made based on the input of the length of 3 sides.

def is_triangle( x , y , z ):

    import math

    if z > x + y:
        return "No"
    elif x > y + z:
        return "No"
    elif y > x + z:
        return "No"
    else:
        return "Yes"

print(is_triangle(22, 10, 10))