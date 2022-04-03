# [----- [김예경] [2021039010] -----]
# hw3: 거북이로 나선형 글자 쓰기
import math
import turtle
import random
from tkinter.simpledialog import *

turtle.title("거북이가 나선 모양의 글자쓰기") #윈도창 제목
turtle.shape('turtle') #거북이 모양으로 설정
turtle.setup(500,500) #윈도창 크기
turtle.screensize(450,450)
turtle.penup() #펜 들어올리기

myStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력') #문자열 입력받기

dist = 200   #떨어진 반지름 길이
angle = 0    #각도

for i in myStr:
    rad = 3.14 * angle / 180 #rad 계산
    tX = dist*math.cos(rad) #x좌표
    tY = dist*math.sin(rad) #y좌표
    turtle.goto(tX,tY) #(x,y)로 이동
    r = random.random(); g = random.random(); b = random.random() #색깔 변수 랜덤으로 고르기
    turtle.pencolor(r,g,b) #색깔 선택
    turtle.write(i, font=('맑은고딕', 20, 'bold')) #글자 작성
    
    dist -= 200/len(myStr)  #반지름의 크기를 점점 줄이기
    angle += 360*2 / len(myStr) #각도의 크기를 점점 늘리기

turtle.done()