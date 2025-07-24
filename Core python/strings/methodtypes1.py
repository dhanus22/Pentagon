class Demo:
    a = 10
    def __init__(self):
        self.b = 20
        self.c = 30
    def instancedisp(self):
        print(self.b)
        print(self.c)

    @staticmethod
    def staticdisp():
        print(Demo.a)

    @classmethod
    def classdisp(cls):
        print("Python")

D1 = Demo()
D1.instancedisp()

Demo.staticdisp()
Demo.classdisp()
