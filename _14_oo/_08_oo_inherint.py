

class Rectangle:
    def __init__(self,
                 width: int,
                 height: int):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side: int):
        self.side = side
        super().__init__(side, side)

s = Square(5)
print(s.area())

class Parallelogram(Rectangle):
    def __init__(self,
                 width: int,
                 height: int):
        self.width = width
        self.height = height
        super().__init__(width, height)

p = Parallelogram(5, 10)
print(p.area())


class Button():
    def __init__(self,
                 text: str,
                 color: int):
        self.text = text
        self.color = color

class GreenButton(Button):
    def __init__(self,
                 text: str):
        super().__init__(text, 0x00FF00)

class WarningButton(Button):
    def __init__(self, text: str, color: int):
        text = text.upper()     #When you specifically want to influence something that's passed on to the parent
        super().__init__(text, color)

class ErrorButton(Button):
    def __init__(self, text: str):
        super().__init__(text, 0xFF0000)

        self.width = 100        #When you want to overrule something from the parent, you put this after the super()