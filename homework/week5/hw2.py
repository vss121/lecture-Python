# [----- [김예경] [2021039010] -----]
# 문자열에서 문자의 발생 빈도 세기
import operator

myText = """
내가 그의 이름을 불러주기 전에는
그는 다만
하나의 몸짓에 지나지 않았다.

내가 그의 이름을 불러주었을 때,
그는 나에게로 와서
꽃이 되었다.

내가 그의 이름을 불러준 것처럼
나의 이 빛깔과 향기에 알맞는
누가 나의 이름을 불러다오.
그에게로 가서 나도
그의 꽃이 되고 싶다.

우리들은 모두
무엇이 되고 싶다.
너는 나에게 나는 너에게
잊혀지지 않는 하나의 눈짓이 되고 싶다."""
myTextDic = {}
#글자의 개수 세기
for i in myText:
    if 'ㄱ' <= i and i <= '힣':
        if i in myTextDic:
            myTextDic[i] += 1
        else:
            myTextDic[i] = 1

#개수를 기준으로 역순으로 정렬하여 list에 저장
sortedList = sorted(myTextDic.items(), key = operator.itemgetter(1), reverse=True)

print("원문" + myText)
print("------------------")
print("문자\t빈도수\t")
print("------------------")
for i in range(len(sortedList)):
    print(sortedList[i][0],'\t', sortedList[i][1])
