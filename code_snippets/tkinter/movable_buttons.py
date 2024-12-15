import tkinter as tk

class MovableButton(tk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bind('<Button-1>', self.on_button_press)
        self.bind('<B1-Motion>', self.on_move)
        self.bind('<ButtonRelease-1>', self.on_button_release)
        self._drag_data = {'x': 0, 'y': 0, 'moved': False}

    def on_button_press(self, event):
        self._drag_data = {'x': event.x, 'y': event.y, 'moved': False}

    def on_move(self, event):
        x = self.winfo_x() - self._drag_data['x'] + event.x
        y = self.winfo_y() - self._drag_data['y'] + event.y
        self.place(x=x, y=y)
        self._drag_data['moved'] = True

    def on_button_release(self, event):
        if not self._drag_data['moved']:
            print(f"{self['text']} action succeeded")

root = tk.Tk()
root.geometry("400x400")

button1 = MovableButton(root, text="Button 1")
button1.place(x=50, y=50)

button2 = MovableButton(root, text="Button 2")
button2.place(x=150, y=150)

root.mainloop()