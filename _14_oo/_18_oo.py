class FlatButton:
    def __init__(self, x, *args, **kwargs):
        if "color" in kwargs:
            self.color = kwargs["color"]

        if "width" in kwargs:
            self.width = kwargs["width"]

class GreenButton(FlatButton):
    def __init__(self, *args, **kwargs):
        if "color" in kwargs:
            del kwargs["color"]

        super().__init__(color="Green", *args, **kwargs)

class StrictSomething:
    def __init__(self, x, y, *args, **kwargs):
        pass

b = GreenButton(width=1, y=2)