#거북이로 구구단 출력하기
import turtle

turtle.title('거북 구구단') #윈도창 제목
turtle.shape('turtle') #거북이 모양으로
turtle.setup(width=800, height=400) #창의 크기
turtle.penup() #펜을 들고 숫자만 그림

for i in range(1,10): #1~9까지 곱할 수
  for j in range(2,10): #2단~9단까지
    turtle.goto(-500+80*j, 200-40*i) #거북이가 반복하면서 위치할 위치
    row = str(j) + ' x ' + str(i) + ' = ' + str(j*i) #한 행
    turtle.write(row,font=('',12)) #거북이로 글씨 출력

turtle.done()
