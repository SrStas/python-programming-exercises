import tkinter as tk
from tkinter import simpledialog


class DrawPathApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Draw Path")

        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()
        self.draw_button = tk.Button(root, text="Draw Path", command=self.draw_path)
        self.draw_button.pack()

    def draw_path(self):
        # Get coordinates from the user
        x1 = simpledialog.askinteger("Input", "Enter x1:", parent=self.root)
        y1 = simpledialog.askinteger("Input", "Enter y1:", parent=self.root)
        x2 = simpledialog.askinteger("Input", "Enter x2:", parent=self.root)
        y2 = simpledialog.askinteger("Input", "Enter y2:", parent=self.root)

        if None in (x1, y1, x2, y2):
            return  # If any input is cancelled, do nothing

        # Draw the line on the canvas
        self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawPathApp(root)
    root.mainloop()
