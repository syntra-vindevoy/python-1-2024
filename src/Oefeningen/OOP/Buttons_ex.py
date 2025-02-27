class FletButton:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        if "color" in kwargs:
            self.color = kwargs["color"]
        if "width" in kwargs:
            self.width = kwargs["width"]

    def press(self):
        print(f"{self.name} is being pressed")

class GreemButton(FletButton):
    def __init__(self, name, *args, **kwargs):

        if "color" in kwargs:
            del kwargs["color"]
        super().__init__(name, color="green", *args, **kwargs)

b = FletButton("Button", color="blue", width=100)
print(b.color)
print(b.width)
b.press()
gb = GreemButton("Button", width=100)
gb.press()
print(gb.color)



