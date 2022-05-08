inFp = None
inStr = ""

inFp = open("data1.txt","r")    #파일 열기, 읽기모드

inStr = inFp.readline() #한 행씩 읽어옴
print(inStr,end="")

inStr = inFp.readline()
print(inStr,end="")

inStr = inFp.readline()
print(inStr, end="")

inFp.close()    #파일 닫기
