#문자열 분리·결합하기 : split(), splitlines(), join()

ss =  "파이썬 열심히 공부 중"
print(ss.split())
ss = "하나:둘"
print(ss.split(":"))
ss = "하나\n둘"
print(ss.splitlines())
ss = "%"
print(ss.join("파이썬"))