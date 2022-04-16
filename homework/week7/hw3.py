from tkinter import *
from tkinter import ttk
#2021039010 김예경
window = Tk()
window.iconbitmap('python.ico') #파이썬 아이콘

baseTab = ttk.Notebook(window)

tabDog = ttk.Frame(baseTab)
baseTab.add(tabDog, text='강아지')
tabCat = ttk.Frame(baseTab)
baseTab.add(tabCat, text = '고양이')

baseTab.pack(expand=1, fill="both")

photoDog = PhotoImage(file = "dog.gif")
labelDog = Label(tabDog, image = photoDog)
labelDog.pack()

photoCat = PhotoImage(file = "cat.gif")
labelCat = Label(tabCat, image = photoCat)
labelCat.pack()

window.mainloop()
