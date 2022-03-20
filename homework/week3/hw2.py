#거북이 서로 만나게 하기
import turtle
import math
import random

t1X, t1Y, t2X, t2Y, t3X, t3Y = [0]*6 #거북이의 X,Y좌표 저장할 변수 초기화
turtle.title('거북이 만나기') #윈도창 제목
turtle.setup(width = 400, height = 400)#창크기 설정

t1 = turtle.Turtle('turtle'); t1.color('red'); t1.penup() #t1은 빨간색 거북이
t2 = turtle.Turtle('turtle'); t2.color('green'); t2.penup() #t2는 초록색 거북이
t3 = turtle.Turtle('turtle'); t3.color('blue'); t3.penup() #t3는 파란색 거북이

t1.goto(-60,-60); t2.goto(0,60); t3.goto(60,-60) #초기 위치 설정
while(1): #만날 때까지 무한반복
  angle = random.randrange(0,360); dist = random.randrange(1,50)
  t1.left(angle); t1.forward(dist) #t1의 움직일 각과 거리를 랜덤으로 지정
  angle = random.randrange(0,360); dist = random.randrange(1,50)
  t2.left(angle); t2.forward(dist) #t2의 움직일 각과 거리를 랜덤으로 지정
  angle = random.randrange(0,360); dist = random.randrange(1,50)
  t3.left(angle); t3.forward(dist) #t3의 움직일 각과 거리를 랜덤으로 지정
  #xcor()과 ycor()함수는 거북이의 X,Y 좌료프를 구함
  t1X = t1.xcor(); t1Y = t1.ycor() #t1의 X,Y 좌표
  t2X = t2.xcor(); t2Y = t2.ycor() #t2의 X,Y 좌표
  t3X = t3.xcor(); t3Y = t3.ycor() #t3의 X,Y 좌표
  #두 거북이의 거리가 가까워지면
  if math.sqrt(((t1X-t2X)*(t1X-t2X))+((t1Y-t2Y)*(t1Y-t2Y))) <=40 or \
    math.sqrt(((t1X-t3X)*(t1X-t3X))+((t1Y-t3Y)*(t1Y-t3Y))) <=40 or \
    math.sqrt(((t2X-t3X)*(t2X-t3X))+((t2Y-t3Y)*(t2Y-t3Y))) <=40 :
    t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3) #거북이의 크기를 3배로
    break #while문을 빠져나감

turtle.done()
