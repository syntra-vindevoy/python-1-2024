class A:
    def __init__(self, *args, **kwargs):
        if "color" in kwargs:
            self.color = kwargs["color"]

        if "width" in kwargs:
            self.width = kwargs["width"]
        print (args)
        print (kwargs)
class B(A):
    def __init__(self, *args, **kwargs):
        if "color" in kwargs:
            del kwargs["color"]

        super().__init__(*args, **kwargs)

b = A("a", color = 1, y = 2, x = 8)







