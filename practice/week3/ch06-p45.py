#1~100의 3의배수 제외한 합
sum, i = 0, 0
for i in range(1,101):
  if i%3==0:
    continue
  sum += i
print(sum)
