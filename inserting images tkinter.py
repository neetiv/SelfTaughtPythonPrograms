from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()

my_image=PhotoImage(file= 'neeti://python.gif')
canvas.create_image(0,0, anchor=NW, image=my_image)


#ask for help on this
