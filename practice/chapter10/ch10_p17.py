#리스트와 for 문 활용
from tkinter import *
window = Tk()

btnList = [None] * 3

for i in range(0,3):
    btnList[i] = Button(window, text="버튼"+str(i+1))

for btn in btnList:
    btn.pack(side=TOP, fill=X)    

window.mainloop()

#side=TOP #side=BOTTOM
#폭 조정 : 
#btn.pack(side=TOP, fill=X)   윈도창 폭 맞춤
#btn.pack(side=TOP, fill=X)