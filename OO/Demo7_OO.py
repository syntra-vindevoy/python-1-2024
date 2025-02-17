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

class Parallelogram(Rectangle):
    def __init__(self, base: int, height: int):
        super().__init__(base, height)


class Button():
    def __init__(self, text: str, color: int):
        self.text = text
        self.color = color

class GreenButton(Button):
    def __init__(self, text: str):
        super().__init__(text, 0x00ff00)

class WarningButton(Button):
    def __init__(self, text: str, color: int):
        text = text.upper()
        super().__init__(text, color)

class ErrorButton(Button):
    def __init__(self, text: str):
        super().__init__(text, 0xff0000)
        self.width = 100


if __name__ == "__main__":
    s = Square(5)
    print(s.surface())
    p = Parallelogram(3, 4)
    print(p.surface())

