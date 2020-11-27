from tkinter import *
from tkinter.colorchooser import *

def NewFile():
    print("New File!")
def OpenFile():
    print("Open File!")
def About():
    print("This is a simple example of a menu")


root = Tk()
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=NewFile)
filemenu.add_command(label="New", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About..",command=About)

canvas = Canvas(root, width=500, height=500)
color = 'red'
result = '#476042'

def callback():
    global result
    result = askcolor(title = "Color Chooser")
    result = result[1]

button = Button(root, text="Choose Color", fg = 'darkgreen',command=callback)
button.pack(side=LEFT, padx=10)

lastx, lasty = 0,0

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx,lasty, event.x,event.y), fill=result)
    lastx, lasty = event.x, event.y

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas.pack()
canvas.bind("<Button-1>",xy)
canvas.bind("<B1-Motion>", addLine)

root.mainloop()
