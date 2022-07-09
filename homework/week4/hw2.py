# 기차 수송량에 따라 순위 매기기

import operator

#전역 변수 선언
trains = [('Saemaeul',5), ('KTX',8), ('Mugunghwa',9), ('ITX',5), ('Saemaeul',4), 
('KTX',7), ('Saemaeul',3),('ITX',8), ('Tongilho',5), ('SRT',13)]
trainDic, trainList = {}, []
rank= 1

#메인 함수
if __name__ == '__main__':

  print("기차 수송량 목록 ==> ", trains)
  print('-------------------------------')
  print('기차\t\t총 수송량 순위')
  print('-------------------------------')

  # 기차 목록에서 같은 기차의 수송량을 합쳐서 새로운 목록 만들기
  for i in range(len(trains)):
    if trains[i][0] in trainDic:              #딕셔너리에 이미 key에 대한 항목이 있다면
      trainDic[trains[i][0]] += trains[i][1]  #있던 value에서 추가
    else:                                     #딕셔너리에 이미 key에 대한 항목이 없다면
      trainDic[trains[i][0]] =trains[i][1]    #새로 value 추가

  # trainDic의 원소들을 trainList에 value을 기준으로 내림차순(reverse=True)으로 정렬
  trainList = sorted(trainDic.items(), key = operator.itemgetter(1), reverse=True)

  # trainList 각 항목들과 순위를 출력하는 부분
  for i in range(len(trainList)):
    print(f'{trainList[i][0]:10s} {trainList[i][1]:>10}', end = '')
    if trainList[i][1] == trainList[i-1][1]:  #같은 수량이 있다면      
        print(f"{rank:>5}")                   #중복이 나오기 전 저장한 값인 rank 출력
    else:                                     #같은 수량이 없다면 
        rank = i+1                            #중복이 나올 경우 사용할 rank 값 바꾸고
        print(f"{i+1:>5}")                    #인덱스+1 값을 등수로 출력
 
