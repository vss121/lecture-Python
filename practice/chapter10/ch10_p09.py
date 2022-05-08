#레이블에 글자 대신 이미지 넣기 /vscode 잘 안됨
from tkinter import *
window = Tk()

photo = PhotoImage(file= "banana.gif") #PhotoImage()는 GIF 파일만
label1 = Label(window, image=photo)

label1.pack()

window.mainloop()
