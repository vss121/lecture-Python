class Car:
    color = ""
    speed = 0

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed
car1 = Car("아우디", 0)
car2 = Car("벤츠", 30)


print("자동차1 색상은 %s, 현재 속도는 %dkm" %(car1.getName(), car1.speed))
print("자동차2 색상은 %s, 현재 속도는 %dkm" %(car2.getName(), car2.speed))

