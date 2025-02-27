class Button:
    def __init__(self, text, color):
        super().__init__()
        self.text = text
        self.color = color

    def click(self):
        print(
            f"Button '{self.text}' clicked with color {self.color}")

class GreenButton(Button):
    def __init__(self, text):
        super().__init__(text, "green")

class OkButton(Button):
    def __init__(self, color):
        super().__init__("OK", color)

class GreenOkButton(GreenButton, OkButton):
    def __init__(self):
        super().__init__("OK")

my_button = GreenOkButton()
my_button.click()