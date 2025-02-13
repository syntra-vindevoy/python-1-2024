class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def surface(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

        self.side = side










class Button:
    def __init__(self, text: str, color: int):
        self.text = text
        self.color = color

class GreenButton(Button):
    def __init__(self, text: str):
        super().__init__(text, 0x00FF00)

class WarningButton(Button):
    def __init__(self, text: str, color: int):
        text = text.upper()

        super().__init__(text, color)

class ErrorButton(Button):
    def __init__(self, text: str):
        super().__init__(text, 0xFF0000)

        self.width = 300


s = Square(5)
print(s.surface())


