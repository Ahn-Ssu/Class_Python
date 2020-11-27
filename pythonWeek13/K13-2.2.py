from tkinter import *
from tkinter import Tk, Canvas
from PIL import ImageTk, Image

root = Tk()
canvas = Canvas(root, width=400, height = 300)
canvas.pack()

def oneclick(event):
    im = Image.open('./pythonWeek13/theMoon.jpg')
    canvas.image = ImageTk.PhotoImage(im)
    canvas.create_image(0,0, image=canvas.image, anchor='nw')

def doubleclick(event):
    im = Image.open('./pythonWeek13/week4Handong 14.jpg')
    canvas.image = ImageTk.PhotoImage(im)
    canvas.create_image(0,0, image=canvas.image, anchor='nw')

widget = Button(None, text="Mouse Clicks")
widget.pack()
widget.bind('<Button-1>',oneclick)
widget.bind('<Double-1>',doubleclick)
root.mainloop()

