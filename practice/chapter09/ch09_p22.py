#덧셈, 뺄셈, 곱셈, 나눗셈을 하는 계산기 함수를 작성

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
    return result

num1, num2, oper, res =0, 0, "", 0

oper = input("연산자를 입력하세요(+,-,*,/) : ")
num1 = int(input("첫 번째 수를 입력하세요 : "))
num2 = int(input("두 번째 수를 입력하세요 : "))
res = calc(num1,num2,oper)
print(f"## 계산기 : {num1} {oper} {num2} = {res}")