class Button:
    def __init__(self, text, color):
        if text is not None:
            self.text = text

        if color is not None:
            self.color = color

    def click(self):
        print("Clicked on a", self.color, "button with text", self.text)

class GreenButton(Button):
    def __init__(self, text = None):
        Button.__init__(self, text, "green")

class OkButton(Button):
    def __init__(self, color = None):
        Button.__init__(self,"OK", color)

class GreenOkButton(GreenButton, OkButton):
    def __init__(self):
        GreenButton.__init__(self)
        OkButton.__init__(self)

print(GreenOkButton.mro())
my_button = GreenOkButton()
my_button.click()