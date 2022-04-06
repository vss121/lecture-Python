#문자열 공백 삭제·변경하기 : strip(), rstrip(), lstrip()
ss = "   파  이  썬   "
print(ss.strip())
print(ss.lstrip())
print(ss.rstrip())

#앞뒤의 특정 문자 삭제 
ss = "----파---이---썬----"
print(ss.strip("-"))
ss = "<<<파<<이>>썬>>>>"
print(ss.strip("<>"))

