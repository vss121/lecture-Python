# 윈도창 조절

from tkinter import *

window = Tk()
window.title('윈도창 연습') #윈도창 제목 표시
window.geometry("400x100")  #윈도창 초기 크기 400*100
window.resizable(width=False, height=False) #가로, 세로 길이 고정

window.mainloop()
