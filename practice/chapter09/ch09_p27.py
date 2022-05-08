# 지역변수, 전역변수 이해하기

def func1():
    a = 10  #지역변수
    print(f"func1()에서 a값 {a}")

def func2():
    print(f"func2()에서 a값 {a}")

a = 20 #전역변수
func1()
func2()