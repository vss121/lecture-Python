num1, num2, op, re = 0, 0, "", 0

while (1):
  num1 = int(input("계산할 첫 번째 수를 입력하세요: "))
  num2 = int(input("계산할 두 번째 수를 입력하세요: "))
  op = input("계산할 연산자를 입력하세요: ")

  if op=='+':
    re = num1 + num2
  elif op=='-':
    re = num1 - num2
  elif op=='*':
    re = num1 * num2
  elif op=='/':
    re = num1 / num2
  elif op=='%':
    re = num1 % num2
  elif op=='//':
    re = num1 // num2
  elif op=='**':
    re = num1 ** num2
  else:
      print("연산자를 잘못 입력했습니다.")

    
  print(f"{num1} {op} {num2} = {re}")
