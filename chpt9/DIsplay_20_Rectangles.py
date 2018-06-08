# This program displays 20 rectangles embedded within each other

from tkinter import *  # Import tkinter


class Rectangle:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Display Rectangles")  # Set title

        frame1 = Frame(window)
        frame1.pack()

        canvas = Canvas(frame1, width=500, height=500)
        canvas.pack()

        for i in range(20):
            canvas.create_rectangle(10 + i * 8, 10 + i * 8, int(canvas["width"]) - 10 - i * 8,
                                    int(canvas["height"]) - 10 - i * 8)

        window.mainloop()  # Create an event loop


Rectangle()