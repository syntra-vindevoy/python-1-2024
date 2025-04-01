class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Operands must be of type Vector")


    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        raise TypeError("Operand must be a number")


    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)



    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

result = v1 + v2  # Calls v1.__add__(v2)
print(result)  # Output: Vector(6, 8)

v1 = Vector(1, 2)
v2 = Vector(1, 2)
v3 = Vector(3, 4)

print(v1 == v2)  # Output: True
print(v1 == v3)  # Output: False

v1 = Vector(5, 7)
v2 = Vector(2, 3)

print(v1 - v2)