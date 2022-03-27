# 2021039010 김예경
# 16진수 정렬하는 프로그램
import random

data = []

# 선택정렬 함수
def selection_sort(arr):
    for i in range(len(arr) - 1): 
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
# 메인함수
if __name__ == '__main__':
  for i in range(5): # 5개의 16진수 데이터를 랜덤으로 뽑기
    data.append(hex(random.randrange(0, 0xFFFF)))
  #정렬 전 데이터 출력  
  print("정렬 전 데이터 : ", end = ' ')
  [print(num, end = ' ') for num in data]  
  selection_sort(data) #선택정렬
  #정렬 후 데이터 출력  
  print("\n정렬 후 데이터 : ", end = ' ')
  [print(num, end = ' ') for num in data]

