inFp = None
inList = ""

inFp = open("data1.txt", "r")

inList = inFp.readlines()   #readlines() 파일의 내용을 통째로 읽어서 리스트에 저장 
print(inList)

inFp.close()
