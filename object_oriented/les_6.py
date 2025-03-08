class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def surface(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side:int):
        super().__init__(side, side)
        self.side = side
s = Square (5)
print (s.surface())

class Parallelogram(Rectangle):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.width = width
        self.height = height

p = Parallelogram(5,6)
print (p.surface())

class Button():
    def __init__(self, text:str, color:int):
        self.text = text
        self.color = color
class GreenButton(Button):
    def __init__(self, text:str):
        self.text = text
        super().__init__(self.text, 0x00ff00)

class Warning(Button):
    def __init__(self, text:str, color:int):
        text = text.upper()
        super().__init__(text, color)

class ErrorButton(Button):
    def __init__(self, text:str):
        super().__init__(text, 0xFF0000)

#x = Warning("error")
print (x.text)