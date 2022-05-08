class Car:
    color = ""
    speed = 0

    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2
    
    def upSpeed(self, value):
        self.speed +=value

    def downSpeed(self, value):
        self.speed -= value
    
myCar1 = Car("red", 30)
myCar2 = Car("blue", 60)

print("자동차1 색상은 %s, 현재 속도는 %dkm" %(myCar1.color, myCar1.speed))
print("자동차2 색상은 %s, 현재 속도는 %dkm" %(myCar2.color, myCar2.speed))

