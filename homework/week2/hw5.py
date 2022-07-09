
#연도를 입력받음
year = int(input("연도를 입력하세요: "))
#윤년일 경우
if ((year%4==0) and (year%100!=0)) or (year%400==0):
    print(f'{year}년은 윤년입니다.')
#아닐 경우
else:
    print(f"{year}년은 윤년이 아닙니다.")

