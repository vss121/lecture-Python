# 덧셈, 뺄셈, 곱셈, 나눗셈, 제곱을 하는 계산기 함수를 작성
# 0으로 나누면 경고 출력

def calc(num1, num2, op):
    result = 0
    if op== '+':
        result = num1 + num2
    elif op== '-':
        result = num1 - num2
    elif op== '*':
        result = num1 * num2
    elif op== '/':
        result = num1 / num2
    elif op== '**':
        result = num1 ** num2    
    return result

num1, num2, oper, res =0, 0, "", 0


num1 = int(input("첫 번째 수를 입력하세요 : "))
oper = input("연산자를 입력하세요(+,-,*,/, **) : ")
num2 = int(input("두 번째 수를 입력하세요 : "))
if (num2==0) and (oper=='/'):
    print("0으로 나누면 안됩니다.")
else:
    res = calc(num1,num2,oper)
    print(f"## 계산기 : {num1} {oper} {num2} = {res}")
