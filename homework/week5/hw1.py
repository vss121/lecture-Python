# [----- [김예경] [2021039010] -----]
# 대소문자 상호 변환하기
ss, res = "", ""
ss = input("문자열을 입력하세요 : ")

for i in ss:
    #대문자일 경우 소문자로 바꾸기
    if i.isupper()==True:
        j = i.lower()
        res += j
    #소문자일 경우 대문자로 바꾸기   
    elif i.islower()==True:
        j = i.upper()
        res += j
    #이외의 경우는 그대로
    else:
        res += i

print("대소문자 변환 결과 =>", res)
