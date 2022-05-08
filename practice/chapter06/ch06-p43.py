#누적 합이 1000이상 되는 시작 지점
sum , i = 0, 1

while(1):
  sum += i
  #print(sum, i)
  if sum>=1000:
    break
  i +=1
print(i)
