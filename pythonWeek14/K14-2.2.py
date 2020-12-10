from tkinter import *
import time

class Circle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_oval(150,150,45,45)
    def move_x(self, x):
        self.x = x
        self.canvas.move(self.id, self.x, 0) 
    def move_y(self, y):
        self.y = y
        self.canvas.move(self.id, 0, self.y) 
    def move_xy(self,x, y):
        self.x = x
        self.y = y
        self.canvas.move(self.id, self.x, self.y)

class f_Circle(Circle):
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,45,45, fill=color)

tk = Tk()
canvas = Canvas(tk, width = 500, height = 400, bd=0, highlightthickness=0)
canvas.pack()

circ = Circle(canvas)
bcirc = f_Circle(canvas, "blue")
rcirc = f_Circle(canvas, "pink")
canvas.pack()

circ.move_x(10)
bcirc.move_xy(150,150)
rcirc.move_y(200)
canvas.pack()