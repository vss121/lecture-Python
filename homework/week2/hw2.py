import sys
#2021039010 김예경

#변수 선언
intVar = 1
floatVar = 1.2
boolVar = True
strVar = ''
listVar = []
tupleVar = ()
dicVar = {}
setVar = set()

#sys.getsizeof()를 이용해서 기본 크기 출력
print('int형 기본 크기 -->', sys.getsizeof(intVar))
print('float형 기본 크기 -->',sys.getsizeof(floatVar))
print('bool형 기본 크기 -->',sys.getsizeof(boolVar))
print('str형 기본 크기 -->',sys.getsizeof(strVar))
print('list형 기본 크기 -->',sys.getsizeof(listVar))
print('tuple형 기본 크기 -->',sys.getsizeof(tupleVar))
print('dictionary형 기본 크기 -->',sys.getsizeof(dicVar))
print('set형 기본 크기 -->',sys.getsizeof(setVar))



