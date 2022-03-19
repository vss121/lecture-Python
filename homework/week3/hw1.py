import random

#전역변수 선언 및 초기화
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
cnt, serial_cnt = 0, 0

while(1):
  cnt+=1 #주사위 던진 횟수 증가
  #6개 주사위를 던짐
  a = random.randrange(1,7)
  b = random.randrange(1,7)
  c = random.randrange(1,7)
  d = random.randrange(1,7)
  e = random.randrange(1,7)
  f = random.randrange(1,7)
  #6개 주사위 모두 같은 수가 나왔을 경우
  if (a==b==c==d==e==f):
    break #무한반복문을 빠져나감
  #1~6의 수가 모두 나왔을 경우
  elif (a==1 or b==1 or c==1 or d==1 or e==1 or f==1) and \
       (a==2 or b==2 or c==2 or d==2 or e==2 or f==2) and \
       (a==3 or b==3 or c==3 or d==3 or e==3 or f==3) and \
       (a==4 or b==4 or c==4 or d==4 or e==4 or f==4) and \
       (a==5 or b==5 or c==5 or d==5 or e==5 or f==5) and \
       (a==6 or b==6 or c==6 or d==6 or e==6 or f==6):
    serial_cnt+=1 #연속번호 나온 횟수 증가

#결과 출력
print("6개 주사위가 모두 동일한 숫자가 나옴 -->",a,b,c,d,e,f)
print("6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 -->",cnt)
print("6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수 -->",serial_cnt)

