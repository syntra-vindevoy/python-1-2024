import tkinter as tk

class MovableButton(tk.Button):
    selected_buttons = []

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bind('<Button-1>', self.on_button_press)
        self.bind('<B1-Motion>', self.on_move)
        self.bind('<ButtonRelease-1>', self.on_button_release)
        self._drag_data = {'x': 0, 'y': 0, 'moved': False}

    def on_button_press(self, event):
        if event.state & 0x0004:  # Control key is pressed
            if self in MovableButton.selected_buttons:
                MovableButton.selected_buttons.remove(self)
            else:
                MovableButton.selected_buttons.append(self)
        else:
            MovableButton.selected_buttons = [self]
        self._drag_data = {'x': event.x, 'y': event.y, 'moved': False}

    def on_move(self, event):
        dx = event.x - self._drag_data['x']
        dy = event.y - self._drag_data['y']
        for button in MovableButton.selected_buttons:
            x = button.winfo_x() + dx
            y = button.winfo_y() + dy
            button.place(x=x, y=y)
        self._drag_data['moved'] = True

    def on_button_release(self, event):
        if not self._drag_data['moved']:
            print(f"{self['text']} action succeeded")

root = tk.Tk()
root.geometry("1920x1080")

button1 = MovableButton(root, text="Button 1\n---\n---")
button1.place(x=50, y=50)

button2 = MovableButton(root, text="Button 2")
button2.place(x=150, y=150)

button3 = MovableButton(root, text="Button 3")
button3.place(x=250, y=250)

root.mainloop()