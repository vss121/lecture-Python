i, k, guguline = 0, 0, ""

for i in range(2,10):
  guguline += ("#   %d단  #" %i)
print(guguline)

for i in range(1,10):
  guguline = ""
  for k in range(2,10):
    guguline += str("%2dX %2d= %2d" %(k,i,i*k))
  print(guguline)

#다시 확인
#문자열 계속 이어서 변수 저장 가능
