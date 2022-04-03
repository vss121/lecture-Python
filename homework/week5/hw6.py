# [----- [김예경] [2021039010] -----]
#hw6: 재귀호출로 진수 구하기

#2진수로 변환
def base2(num):
    if(num>1):
        base2(num//2)
    print(num%2, end=' ')

#8진수로 변환
def base8(num):
    if(num>7):
        base8(num//8)
    print(num%8, end=' ')

#16진수로 변환
def base16(num):
    if(num>15):
        base16(num//16)
    print(num%16, end=' ')

if __name__ == '__main__':
    myNum = int(input("10진수 입력 -> "))
    print("2진수 :",end=' '); base2(myNum); print() #2진수 출력
    print("8진수 :",end=' '); base8(myNum); print() #8진수 출력
    print("16진수 :",end=' '); base16(myNum); print() #16진수 출력