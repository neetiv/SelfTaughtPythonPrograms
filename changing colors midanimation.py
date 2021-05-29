from tkinter import *
import time
import random

tk = Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()
colors=['green', 'red', 'blue', 'orange','yellow','cyan','magenta','violet','purple','pink']

triangle=canvas.create_polygon(10,10,10,60,50,35, fill=random.choice(colors))
canvas.move(triangle, 5, 0)

while True:
    for i in range(0,60):
        canvas.move(1, 5, 5)
        tk.update()
        time.sleep(0.03)
        
    canvas.itemconfig(triangle, fill=random.choice(colors))
    
    for i in range(0,60):
        canvas.move(1,-5,-5)
        tk.update()
        time.sleep(0.03)

    canvas.itemconfig(triangle, fill=random.choice(colors))
