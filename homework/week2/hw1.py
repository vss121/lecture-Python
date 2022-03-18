import turtle
import random

#2021039010 김예경

#마우스 우클릭시 실행하는 함수
def screenRightClick(x,y):
    turtle.goto(x,y) #거북이를 이동시킴
    
    #랜덤으로 정하는 선의 색상을 저장하는 변수들
    r= random.random()
    g= random.random()
    b= random.random()
    #랜덤으로 정하는 거북이 크기를 저장하는 변수
    tSize = random.randrange(1,10)
    #랜덤으로 정하는 거북이 각도를 저장하는 변수
    tAngle = random.randrange(0,360)
    
    turtle.pencolor(r,g,b) #펜의 랜덤한 색상 설정
    turtle.color(r,g,b) #거북이의 랜덤한 색상 설정
    turtle.shapesize(tSize) #거북이의 랜덤한 크기 설정
    turtle.right(tAngle) #거북이의 랜덤한 각도 설정
    turtle.stamp() #거북이의 도장이 찍힘

turtle.title('거북이 도장 찍기 프로그램') #윈도창 제목 설정
turtle.shape('turtle') #모양을 거북이로 설정
turtle.onscreenclick(screenRightClick,3) #마우스 우클릭하면 위의 함수를 실행

turtle.done()
