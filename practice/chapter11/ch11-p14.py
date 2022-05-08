inFp = None
inStr = ""

inFp = open("data1.txt", "r")

while True: #무한 반복
    inStr = inFp.readline() #한 행 읽음
    if inStr == "":     #읽어온게 없다면
        break;  #반복문 빠져나옴
    print(inStr, end="")

inFp.close()
