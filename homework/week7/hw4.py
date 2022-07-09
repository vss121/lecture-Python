from tkinter import *
from tkinter.filedialog import *


def func_open():
    global filename
    filename = askopenfilename(parent = window, filetypes = (("GIF파일", "*.gif"),
                ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy() 

def KeyClick(event):
    global key
    key=event.keysym
    if key=='Up':
        func_zoom()
    elif key=='Down':
        func_subsample()

def func_zoom():
    global photo
    photo = PhotoImage(file = filename)
    photo = photo.zoom(3,3)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_subsample():
    global photo
    photo = PhotoImage(file = filename)
    photo = photo.subsample(3,3)
    pLabel.configure(image = photo)
    pLabel.image = photo

window = Tk()
window.geometry("400x400")
window.title("확대, 축소하기")

photo = PhotoImage()
pLabel = Label(window,image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

window.bind("<Key>",KeyClick)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.mainloop()
