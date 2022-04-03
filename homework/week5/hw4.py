# [----- [김예경] [2021039010] -----]
# 문자와 숫자가 섞인 데이터 정렬하기
import random
myData = []
myNumData = []
mySortedData = []

#n개의 수를 랜덤으로 뽑는 함수
def importNumber(n):
    for i in range(n): #n번 반복
        temp = hex(random.randrange(0,100000)) #랜덤으로 16진수 뽑음
        myData.append(temp[2:]) #리스트에 뽑은 값 첨가

#값에서 숫자만 추출한 리스트 만들기
def getNumber(arr):
    global myNumData
    for i in range(len(arr)):
        ss = ""
        for j in range(len(arr[i])):
            #문자열에서 숫자일 경우 그 숫자만 모아서 문자열로 만들기
            if arr[i][j].isdigit():
                ss += arr[i][j]
        myNumData.append(ss) #문자열을 리스트에 추가하기
    #리스트 안에 들어있는 string을 int로 바꾸기
    myNumData = list(map(int, myNumData)) 

#선택정렬하는 함수
def selection_sort(arr):
    global mySortedData
    for i in range(0, len(arr)-1):
        idx = i
        for j in range(i+1, len(arr)):
            if arr[idx] > arr[j]:
                idx = j
        arr[idx], arr[i] = arr[i], arr[idx]
    mySortedData = list(arr)

#메인함수           
if __name__ == "__main__":
    importNumber(10) #10개의 수를 뽑기
    #정렬 전 데이터 출력
    print("정렬 전 데이터: ", end ='')
    [print(i, end=' ') for i in myData]

    getNumber(myData) #숫자만 추출하기
    selection_sort(myNumData) #선택정렬하기
    print()
    #정렬 후 데이터 출력
    print("정렬 후 데이터: ", end ='')
    [print(i, end=' ') for i in mySortedData]
