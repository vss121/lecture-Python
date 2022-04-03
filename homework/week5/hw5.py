# [----- [김예경] [2021039010] -----]
#hw5: 날짜 세기 및 요일 구하기

from time import *
from datetime import *

#날짜 세기
def countDays(d1, d2):
    year, month, day = d1.split('/')
    Day1 = date(int(year), int(month), int(day))
    year, month, day = d2.split('/')
    Day2 = date(int(year), int(month), int(day))
    diffDays = Day2- Day1
    retDays = diffDays.days
    return retDays

#요일 세기
def daysOfWeek(d):
    dotw = ['월','화','수','목','금','토','일']
    return dotw[d.tm_wday]

if __name__=="__main__":
    myDate = input("시작날짜(연/월/일): ")
    tm = localtime()
    curDate = str(tm.tm_year) + '/' + str(tm.tm_mon) + '/' + str(tm.tm_mday)
    print(str(myDate) + '부터 오늘 ' + str(curDate) +'까지는 '+ str(countDays(myDate,curDate))+'일이 지났습니다.')
    print('오늘은 ' + str(daysOfWeek(tm)) + '요일입니다.')