#마우스 왼쪽 버튼을 클릭했을 때 처리하는 방법
from tkinter import *
from tkinter import messagebox

def clickLeft(event):
    messagebox.showinfo("마우스","왼쪽 클릭")

window = Tk()
#위젯.bind("마우스 이벤트", 이벤트처리함수))
window.bind("<Button-1>",clickLeft)

window.mainloop()