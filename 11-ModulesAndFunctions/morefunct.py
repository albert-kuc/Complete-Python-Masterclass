"""
    Program created following tutorials:
    97. Parabola - More on Functions
    98. Scope in functions
    99. Fix functions and draw circles
"""

import math
try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot (page, x, y)
        plot (page, -x, y)


def circle(page, radius, g, h):
    for x in range(g, g+radius):
        y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
        plot(page, x, y)
        plot(page, x, 2 * h - y)
        plot(page, 2 * g - x, y)
        plot(page, 2 * g - x, 2 * h - y)


def draw_axex(page):
    page.update()
    x_origin = page.winfo_width() /2
    y_origin = page.winfo_height() /2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="white")
    page.create_line(0, y_origin, 0, -y_origin, fill="white")


def plot(canvas, x, y):
    canvas.create_line(x, -y, x + 1, -y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axex(canvas)

parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100)


mainWindow.mainloop()