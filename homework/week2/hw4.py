
#string1이라는 변수에 입력받음
string1 = input("문자열을 입력 --> ")
#문자열을 리스트로 변환
string2 = list(string1)
#리스트를 역순으로
string2.reverse()
#리스트를 문자열로 변환
string3 = ''.join(string2)
#역순 문자열 출력       
print(string3)
