# 2021039010 김예경
# 거북이 리스트 활용(정렬)
import turtle
import random

# 전역변수 선언
myTurtle, tX, tY, tColor, tSize, tShape, tAngle = [None] * 7
playerTurtles = []
swidth, sheight = 500, 500


# 메인함수
if __name__ == "__main__":
  turtle.title('거북 리스트 활용(정렬)')                   #창 이름
  turtle.setup(width = swidth + 100, height = sheight + 100) #창 크기
  turtle.screensize(swidth, sheight)                        #캔버스 크기

  for i in range(0, 5):
    myTurtle = turtle.Turtle('turtle')            #모양을 거북이로 설정
    tX = random.randrange(-swidth/2, sheight/2)   #x좌표 랜덤으로 설정
    tY = random.randrange(-swidth/2, sheight/2)   #x좌표 랜덤으로 설정
    r = random.random()                        #rgb의 r색상 랜덤으로 설정
    g = random.random()                        #rgb의 g색상 랜덤으로 설정
    b = random.random()                        #rgb의 b색상 랜덤으로 설정
    tSize = random.randrange(1, 100)/10           #거북이 크기 설정(1.0~9.9)
    tAngle = random.randrange(0, 360)             #거북이 각도 설정(0~360)
    #playerTurtles라는 2차원 리스트에 거북이 속성을 담은 1차원 리스트를 반복하여 첨가
    playerTurtles.append([myTurtle,tX, tY, tSize, r,g,b, tAngle])
      
  # 위 리스트에서 tSize라는 4번째 요소를 기준으로 오름차순으로 정렬.
  # sorted( list나 dict, key = lambda x : (key로 지정하고 싶은 요소) ) 이용
  sortedTurtles = sorted(playerTurtles, key = lambda turtles : turtles[3])

  for i, v in enumerate(sortedTurtles):      #enumerate()은 index와 그 원소를 tuple 형태로 반환
    myTurtle = v[0]                         #거북이 모양 설정
    myTurtle.color(v[4],v[5],v[6])          #거북이 r,g,b 색상 설정
    myTurtle.pencolor(v[4],v[5],v[6])       #펜 r,g,b 색상 설정
    myTurtle.turtlesize(v[3])               #거북이 크기 설정
    myTurtle.right(v[7])                    #거북이 각도 설정
    myTurtle.penup()                        #그리지 않고 이동
    if i == 0:                              #첫 번째 거북이일 경우
      myTurtle.goto(v[1],v[2])              #첫 번째 위치로 이동
    else:
      myTurtle.goto(sortedTurtles[i-1][1], sortedTurtles[i-1][2]) #앞 거북이의 좌표로 이동해서 선을 그음
      myTurtle.pendown()
      myTurtle.goto(v[1],v[2]) #자기 원래 좌표로 이동

  turtle.done()
      
                           
