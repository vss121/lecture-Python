from tkinter import *
#2021039010 김예경
#버튼 클릭 시
def myFunc():
  if var.get() == 1:
      labelImage.configure(image = photo1)
  elif var.get() == 2:
      labelImage.configure(image = photo2)
  else :
      labelImage.configure(image = photo3)


var, labelImage = 0, None
photo1, photo2, photo3 = [None] *3

if __name__ == "__main__":
  window = Tk() #창 만들기
  window.geometry("400x400")  #창 크기
  window.title("애완동물 선택하기") #창 제목
  labelText = Label(window, text = "좋아하는 동물 투표", fg="blue", font=("궁서체", 20))

  var = IntVar()
  rb1 = Radiobutton(window, text="강아지", variable=var, value=1)
  rb2 = Radiobutton(window, text="고양이", variable=var, value=2)
  rb3 = Radiobutton(window, text="토끼", variable=var, value=3)
  buttonOk = Button(window, text="사진 보기", command = myFunc)

  photo1 = PhotoImage(file="dog.gif")
  photo2 = PhotoImage(file="cat.gif")
  photo3 = PhotoImage(file="rabbit.gif")

  labelImage = Label(window, width=200, height=200, bg="Yellow", image=None)

  labelText.pack(padx=5, pady=5)
  rb1.pack(padx=5, pady=5)
  rb2.pack(padx=5, pady=5)
  rb3.pack(padx=5, pady=5)
  buttonOk.pack(padx=5, pady=5)
  labelImage.pack(padx=5, pady=5)

  window.mainloop()
