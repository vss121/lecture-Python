# 지정된 위젯을 클릭했을 때 다른 함수 호출
from tkinter import *
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo("마우스", "그림 클릭됨")

window = Tk()
window.geometry("400x400")

photo = PhotoImage(file= "banana.gif")
label1 = Label()