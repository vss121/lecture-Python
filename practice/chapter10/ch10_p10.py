#이미지 2개 출력 
from tkinter import *
window = Tk()

photo1 = PhotoImage(file= "banana.gif") #PhotoImage()는 GIF 파일만
label1 = Label(window, image=photo1)
photo2 = PhotoImage(file= "banana.gif") #PhotoImage()는 GIF 파일만
label2 = Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack()

window.mainloop()