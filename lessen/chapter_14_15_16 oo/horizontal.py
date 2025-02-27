class Button:
    def __init__(self, color=None, text=None):
        self.color = color
        self.text = text
        print("Button initialized with color:", self.color, "and text:", self.text)

    def click(self):
        print("Button clicked")


class OKButton(Button):
    def __init__(self):
        super().__init__(text="ok")
        print("OK Button initialized with text:", self.text)

    def click(self):
        print("OK Button clicked")


class GreenButton(Button):
    def __init__(self):
        super().__init__(color="green")
        print("Green Button initialized with color:", self.color)

    def click(self):
        print("Green Button clicked")


class GreenOKButton(OKButton, GreenButton):
    def __init__(self):
        OKButton.__init__(self)
        GreenButton.__init__(self)
        print(
            "Green OK Button initialized with text:",
            self.text,
            "and color:",
            self.color,
        )

    def click(self):
        print("Green OK Button clicked")


# Testing the classes
if __name__ == "__main__":
    button = Button()
    ok_button = OKButton()
    green_button = GreenButton()
    green_ok_button = GreenOKButton()

    button.click()
    ok_button.click()
    green_button.click()
    green_ok_button.click()
