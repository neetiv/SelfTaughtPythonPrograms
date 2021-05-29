## drawing random polygons

import random
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width = 700, height = 250)
canvas.pack()

colors = ['green', 'red', 'blue', 'orange', 'yellow', 'cyan', 'pink', 'purple', 'violet', 'magenta']

#triangle
canvas.create_polygon(20,20,100,20,100,120, fill=random.choice(colors), outline=random.choice(colors))


#double triangle thing
canvas.create_polygon(200,10,240,30,120,100,140,120, fill=random.choice(colors), outline=random.choice(colors))

#pentagon?
canvas.create_polygon(350,100,400,10,450,100,425,200,375,200, fill=random.choice(colors), outline=random.choice(colors))
