class A:
    def dispA(self):
        print("Inside dispA")

class B(A):
    def dispB(self):
        print("Inside dispB")

class C(A):
    def dispC(self):
        print("Inside dispC")


c1 = C()
b1 = B()
c1.dispC()
c1.dispA()
b1.dispB()
b1.dispA()
