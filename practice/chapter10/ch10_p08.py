#레이블(Label) : 문자를 표현할 수 있는 위젯

from tkinter import *
window = Tk()

label1 = Label(window, text="python을") #label()은 레이블을 만들어 줌
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")   #font 글꼴과 크기
label3 = Label(window, text="공부 중입니다", bg="magenta", width=20, height=5, anchor=SE)   #bg 배경색 #anchor 위젯의 위치

label1.pack()   #pack()은 해당 레이블을 화면에 표시
label2.pack()
label3.pack()

window.mainloop()