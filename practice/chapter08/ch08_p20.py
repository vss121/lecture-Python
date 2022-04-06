ss = input("날짜(연/월/일) 입력 =>")

ssList = ss.split('/')

print(f"입력한 날짜의 10년 후=> {int(ssList[0])+10}년{ssList[1]}월{ssList[2]}일")