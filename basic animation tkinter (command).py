import time
from tkinter import *
tk=Tk()

canvas=Canvas(tk, width=400, height=400)
canvas.create_polygon(10,10,10,60,50,35, fill='violet')
canvas.pack()

def move(event):
    if event.keysym == 'Up':
        canvas.move(1,0,-5)
    elif event.keysym == 'Down':
        canvas.move(1,0,5)
    elif event.keysym == 'Right':
        canvas.move(1,5,0)
    else:
        canvas.move(1,-5,0)

canvas.bind_all('<KeyPress-Up>', move)
canvas.bind_all('<KeyPress-Down>', move)
canvas.bind_all('<KeyPress-Right>', move)
canvas.bind_all('<KeyPress-Left>', move)
