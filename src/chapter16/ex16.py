""""
16.10.2. Exercise
Write an __eq__ method for the Line class that returns True if the Line objects refer to Point objects that are equivalent, in either order.
"""
from copy import copy

"""
16.10.3. Exercise
Write a Line method called midpoint that computes the midpoint of a line segment and returns the result as a Point object.
"""
"""
16.10.4. Exercise
Write a Rectangle method called midpoint that find the point in the center of a rectangle and returns the result as a Point object.
"""
"""
16.10.5. Exercise
Write a Rectangle method called make_cross that:

Uses make_lines to get a list of Line objects that represent the four sides of the rectangle.

Computes the midpoints of the four lines.

Makes and returns a list of two Line objects that represent lines connecting opposite midpoints, forming a cross through the middle of the rectangle.
"""


class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def translated(self, dx=0, dy=0):
        point = copy(self)
        point.translate(dx, dy)
        return point

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'Line({self.p1}, {self.p2})'

    def __repr__(self):
        return f'Line({self.p1}, {self.p2})'

    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2

    def draw(self):
        pass

    def midpoint(self):
        return Point((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)


class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """

    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self):
        return f'Rectangle({self.width}, {self.height}, {self.corner})'

    def make_points(self):
        p1 = self.corner
        p2 = p1.translated(self.width, 0)
        p3 = p2.translated(0, self.height)
        p4 = p3.translated(-self.width, 0)
        return p1, p2, p3, p4


    def make_lines(self):
        p1, p2, p3, p4 = self.make_points()
        return Line(p1, p2), Line(p2, p3), Line(p3, p4), Line(p4, p1)

    def draw(self):
        lines = self.make_lines()
        for line in lines:
            line.draw()


    def grow(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight

    def midpoint(self):
        p1,p2,p3,p4 = self.make_lines()
        p1_mid = p1.midpoint()
        p2_mid = p2.midpoint()
        p3_mid = p3.midpoint()
        p4_mid = p4.midpoint()
        return Point((p1_mid.x + p2_mid.x + p3_mid.x + p4_mid.x) / 4, (p1_mid.y + p2_mid.y + p3_mid.y + p4_mid.y) / 4)

    def make_cross(self):
        p1,p2,p3,p4 = self.make_lines()
        p1_mid = p1.midpoint()
        p2_mid = p2.midpoint()
        p3_mid = p3.midpoint()
        p4_mid = p4.midpoint()
        return Line(p1_mid, p2_mid), Line(p3_mid, p4_mid)