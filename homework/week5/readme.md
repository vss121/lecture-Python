5주차 과제 (22-04-03 제출) 
====
* 몰랐거나 배운 부분 정리하기


#hw1: 대소문자 상호 변환하기
-----
* string1.upper() // string2.lower() // string3.swapcase()   
* __<built-in method isupper of str object at 0x000002F84EC0A8F0>__   
upper가 아닌 upper()로 사용해야 함!!  

#hw2: 문자열에서 문자의 발생 빈도 세기
----
- [ ] 다시  
* 개수 세서 딕셔너리에 넣는 방법   
```python 
for i in myText:
    if 만족시키려는 조건문:
        if i in myTextDic:  #글자가 있을 때는 하나 추가
            myTextDic[i] += 1
        else:               #글자가 없을 때는 1로 하기
            myTextDic[i] = 1
```
* 딕셔너리의 값을 기준으로 정렬하는 방법
  * items()는 딕셔너리의 key, value 모두 얻음   
  * import operator  operator.itemgetter(1)은 item인 튜플의 2번째 요소 기준으로   
  * reverse=True는 내림차순으로
```python 
sortedList = sorted(myTextDic.items(), key = operator.itemgetter(1), reverse=True)
```

#hw3: 거북이로 나선형 글자 쓰기
---
- [ ] 다시  
* Tkinter를 사용하여 GUI 만들기(메뉴와 대화상자)   
```python 
from tkinter.simpledialog import *
myStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
```

#hw4: 문자와 숫자가 섞인 데이터 정렬하기
----
* 대괄호 없이 리스트의 값만 출력하기  
[print(i, end=' ') for i in myData]  
* local variable 'ss' referenced before assignment  
전역변수를 지역변수로 사용할 때 발생하는 오류  
내가 만든 함수 안에서 전역변수를 사용할 때 선언을 해줘야 함  
global 변수로 수정하기 

* list 복사 하는법  
list2 = list1[:] #슬라이싱  
list2 = list(list1) #list() 함수  
list2 = list1.copy() #copy 메소드  
list2 = [ ] + list1 #연산  

* 문자열을 조합해서 만들 때  
ss += 추가할 문자 
이용하면 편함  

* 문자열 목록을 정수로 변환  
int_list = list(map(int, string_list))  

#hw5: 날짜 세기 및 요일 구하기
---
- [ ] 다시  
localtime() #현재지역 시간   
tm_year 연 예: 1993, 2019  
tm_mon 달 범위: 1\~12  
tm_mday 일 범위: 1\~31  
tm_hour 시 범위: 0\-23  
tm_min 분 범위: 0\~59  
tm_wday 요일 범위: 0\~6 (0: 월요일)  
* from datetime import *   
  * datetime.date(y,m,d)  
  * 두 날짜의 차이   
```python 
>>> diff = day1 - day2
>>> diff
datetime.timedelta(days=9324)
>>> diff.days
9324
```

#hw6: 재귀호출로 진수 구하기
---
* 10진수 -> 다른 진수로 변환  
> bin(42)  
'0b101010'  
> oct(42)  
'0o52'  
> hex(42)  
'0x2a'  

* 재귀함수로 2진수 변환   
```python
def base2(num):
    if(num>1):
        base2(num//2)
    print(num%2, end=' ')
```   

