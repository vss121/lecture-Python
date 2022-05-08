class Car:
    color = ""
    speed = 0

    def upSpeed(self,value):
        self.speed += value
    def downSpeed(self,value):
        self.speed -= value

mycar1 = Car()
mycar1.color = "red"
mycar1.speed = 0

mycar2 = Car()
mycar2.color = "blue"
mycar2.speed = 0

mycar3 = Car()
mycar3.color = "green"
mycar3.speed = 0

mycar1.upSpeed(30)
print("자동차1 색상은 %s, 현재 속도는 %dkm" %(mycar1.color, mycar1.speed))

mycar2.upSpeed(60)
print("자동차2 색상은 %s, 현재 속도는 %dkm" %(mycar2.color, mycar2.speed))

mycar3.upSpeed(0)
print("자동차3 색상은 %s, 현재 속도는 %dkm" %(mycar3.color, mycar3.speed))
