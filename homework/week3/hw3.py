#하트 모양 출력하기
num = int(input("숫자를 여러 개 입력하세요 : ")) #입력한 숫자를 저장할 변수
num_list = list(map(int, str(num))) #각 자리수를 리스트로 변환

for i in num_list: #앞에서 한 자리부터
  for j in range(i): #각 자릿수 만큼 하트로 출력
    print('\u2665',end='')
  print('')
