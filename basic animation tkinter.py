import time
from tkinter import *
tk=Tk()

canvas=Canvas(tk, width=400, height=400)
canvas.create_polygon(10,10,10,60,50,35, fill='magenta')
canvas.pack()

while True:
    for i in range(0,60):
        canvas.move(1,5,5)
        tk.update()
        time.sleep(0.03)
        
    for i in range(0,60):
        canvas.move(1,-5,-5)
        time.sleep(0.001)
