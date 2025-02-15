class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return super().area()

    def __str__(self):
        return f"Square({self.width})"


class Parallelogram(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def area(self):
        return super().area()

    def __str__(self):
        return f"Parallelogram({self.width}, {self.height})"


class Button:
    def __init__(self, x, y, width, height, text: str):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = 'white'


class GreenButton(Button):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, 'green')

    def __str__(self):
        return f"GreenButton({self.x}, {self.y}, {self.width}, {self.height}, {self.text})"


class WarningButton(Button):
    def __int__(self, x, y, width, height,text:str):

        super().__init__(x, y, width, height, text)
        super.color = 'yellow'

    def __str__(self):
        return f"WarningButton({self.x}, {self.y}, {self.width}, {self.height}, {self.text})"


if __name__ == "__main__":
    # Example usage of Rectangle
    rectangle = Rectangle(5, 10)
    print(rectangle)  # Rectangle(5, 10)
    print(f"Area: {rectangle.area()}")  # Area: 50
    print(f"Perimeter: {rectangle.perimeter()}")  # Perimeter: 30

    # Example usage of Square
    square = Square(4)
    print(square)  # Square(4)
    print(f"Area: {square.area()}")  # Area: 16
    print(f"Perimeter: {square.perimeter()}")  # Perimeter: 16

    # Example usage of Parallelogram
    parallelogram = Parallelogram(6, 8)
    print(parallelogram)  # Parallelogram(6, 8)
    print(f"Area: {parallelogram.area()}")  # Area: 48
    print(f"Perimeter: {parallelogram.perimeter()}")  # Perimeter: 28

    green = GreenButton(5, 2, 5, 6)
    print(green)
    yellow = WarningButton(5, 2, 5, 6,"warning")
    print(yellow)
