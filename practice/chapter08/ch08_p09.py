inStr, outStr = "", ""
i = 0

inStr = input("문자열을 입력하세요: ")

for i in range(len(inStr)):
    outStr += inStr[len(inStr)-(i+1)]   #문자열을 입력받아 반대로 출력

print("내용을 거꾸로 출력 ->", outStr)
