#문자열 찾기 : count(), find(), rfind(), index(), rindex(), startswith(), endswith()
ss = "파이썬 공부는 즐겁습니다. 공부."
print(ss.count("공부"))
print(ss.find("공부"),ss.rfind("공부"),ss.find("공부",5),ss.find("없다"))
print(ss.index("공부"),ss.rindex("공부"),ss.index("공부"),5)
print(ss.startswith("파이썬"),ss.startswith("파이썬",10),ss.endswith("."))