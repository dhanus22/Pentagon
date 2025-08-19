class Radio:
    def turnOn(self,x):
        if (x == 1):
            print("Radio is ON")
        else:
            print("Radio is Off")

class Car:
    def __init__(self,min,max):
        self.min = min
        self.max = max
        self.r = Radio()

c = Car(60,120)
print(c.max)
print(c.min)
c.r.turnOn(1)
c.r.turnOn(2)