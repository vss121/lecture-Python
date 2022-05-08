class Car:
    color = ""
    speed = 0

    def __init__(self):
        self.color = "red"
        self.speed = 0
    
    def upSpeed(self, value):
        self.speed +=value

    def downSpeed(self, value):
        self.speed -= value
    
myCar1 = Car()
myCar2 = Car()

print("자동차1 색상은 %s, 현재 속도는 %dkim" %(myCar1.color, myCar1.speed))
print("자동차2 색상은 %s, 현재 속도는 %dkim" %(myCar2.color, myCar2.speed))

