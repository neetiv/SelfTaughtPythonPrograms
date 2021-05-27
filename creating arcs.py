## creating arcs

from tkinter import *
arcs = Tk()
canvas = Canvas(arcs, width=400, height=400)
canvas.pack()

y_one = 10
y_two = 80

def CreateArc(x1, y1, x2, y2, Extent, Style):
    canvas.create_arc(x1, y1, x2, y2, extent=Extent, style=Style)


for i in range (0, 5):
    CreateArc(10, y_one, 200, y_two)
    y_two = y_two + 80

    if i == 0:
        y_one = y_one + 70
    else:
        y_one = y_one + 80
