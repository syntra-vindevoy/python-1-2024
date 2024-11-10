from copy import copy


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


if __name__ == '__main__':
    start = Point(0, 0)
    end1 = copy(start)
    end1.translate(300, 0)
    print(end1)
    end2 = start.translated(0, 150)
    print(end2)
    print(Line(Point(0, 0), Point(300, 0)))
    p1 = Point(200, 100)
    p2 = Point(200, 100)
    print(p1 == p2)
    print(p1 is p2)
    corner = Point(30, 20)
    box1 = Rectangle(100, 50, corner)
    print(box1)
    box2 = copy(box1)
    box2.grow(60, 40)
    print(box2)
    line1 = Line(start, end1)
    print(line1)
    line2 = Line(start, end2)
    print(line2)

    line1.draw()
    line2.draw()
    box1.draw()

    corner = Point(20, 20)
    box3 = Rectangle(100, 50, corner)
    print(box3)
    from copy import deepcopy

    box4 = deepcopy(box3)

    print(box3.corner is box4.corner)

    shapes = [line1, line2, box3, box4]

    for shape in shapes:
        shape.draw()