from tkinter import *
import random
import time

tk=Tk()
tk.title("~bouncy ball~") #title of window
tk.resizable(0,0) #size of the window cannot be changed
tk.wm_attributes("-topmost", 1) #window will go to the front of all other open windows

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
#bd and highlightthickness remove the border from the canvas
canvas.pack()
tk.update()

colorlist=['green','red','blue','orange','yellow','pink','purple','violet','magenta','cyan','black','white']

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id, 245, 100)
        
        self.x = 0
        self.y = -1 #x and y pos of the ball
        self.canvas_height = self.canvas.winfo_height() #winfo_height returns the current height of the canvas

    def draw(self):
        self.canvas.move(self.id, self.x, self.y) #call the move funciton
        pos = self.canvas.coords(self.id) #create pos variable; coords returns the cuurent x+y pos of any object on the screen

        if pos[1] <= 0:
            self.y = 1 #if you hit the top of the screen stop subtracting 1 from y1(the top of the ball)
        if pos[3] >= self.canvas_height:
            self.y = -1 #if y2(bottom of the ball) touches bottom of the screen set y1 back to -1
            
        #significance of pos[x] -> [y1, x1, y2, x2]

ball = Ball(canvas, random.choice(colorlist))

while True:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)#this number affects ball speed
    #redraws the screen every one-hundreth of a second

