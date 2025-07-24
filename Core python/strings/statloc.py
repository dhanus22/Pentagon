class Demo:
    x = 10
    def __init__(self):
        self.y = 20
        self.z = 30
    def add(self):
        a = 100
        b = 200
        c = a + b
        print(c)
d1 = Demo()
print(d1.y)
print(d1.z)

d1.add()

n1 = 15
print(n1)
print(Demo.x)