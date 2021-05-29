from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=700, height=400)
canvas.pack()

canvas.create_text(100,100, text="Hola")
canvas.create_text(100,150, text="<3", fill='red')
canvas.create_text(150,200, text="Bienvenido a mi python program!", font=('Times', 17))
canvas.create_text(175,250, text="Hay una silla aqui.", font=("Helvetica", 20))
canvas.create_text(250,300, text="Voy a la consulta hoy.", font=("Courier", 30))
canvas.create_text(250,350, text="Tengo un fiebre pequena. :/", font=("Courier", 25), fill="blue")
