from tkinter import *
from tkinter import messagebox

root = Tk()

def forward():
    global currentImage
    if currentImage == 3: #end
        messagebox.showinfo('에러', '마지막 사진입니다')
    else:
        currentImage =  currentImage+1
        lbPhoto['image'] = img[currentImage]
        photoname.set(name[currentImage])
def backward():
    global currentImage
    if currentImage == 0: #first
        messagebox.showinfo('에러', '첫번째 사진입니다')
    else:
        currentImage =  currentImage-1
        lbPhoto['image'] = img[currentImage]
        photoname.set(name[currentImage])

currentImage=0

# 사진 액자
frame = Frame(root, padx=10, pady=10, borderwidth=2, relief='sunken',
              width=500, height=400)
frame.grid_propagate(False)
frame.grid(row=1, column=1)

# 사진 설명
name = ['꽃','겨울', '도시', '바다']
photoname=StringVar()
lbName = Label(frame, textvariable=photoname)
photoname.set(name[currentImage])
lbName.pack()

# 이미지를 2개 --> label
img1 = PhotoImage(file="image\\flower.gif")
img2 = PhotoImage(file="image\\winter.gif")
img3 = PhotoImage(file="image\\building.gif")
img4 = PhotoImage(file="image\\sea.gif")
img = [img1, img2, img3, img4]

lbPhoto = Label(frame)
lbPhoto['image'] = img[currentImage]
lbPhoto.pack()

# 앞으로 뒤로 버튼
bb = Button(root, text='<<', command=backward)
bb.grid(row=1, column=0, padx=5)
bf = Button(root, text='>>', command=forward)
bf.grid(row=1, column=2, padx=5)

root.mainloop()
