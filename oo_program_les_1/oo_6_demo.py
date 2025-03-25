class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


#class Rectangle:
    #def __init__(self, p1: point, p2: point, p3: point, p4: point):
        #self.p1 = p1
        #self.p2 = p2
        #self.p3 = p3
        #self.p4 = p4

class Rectangle:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height

    def surface(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side:int):
        super().__init__(side, side)
        self.side = side

class Parallellogram(Rectangle):
    def __init__(self, width:int, height:int):
        super().__init__(width, height)


class Button:
    def __init__(self, text: str, color: str):
        self.text = text
        self.color = color

class GreenButton(Button):
    def __init__(self, text: str):
        super().__init__(text, 0X00FF00)

s = Square(5)

print(s.surface())

p = Parallellogram(5, 10)
print(p.surface())

