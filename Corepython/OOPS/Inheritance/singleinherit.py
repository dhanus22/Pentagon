class A:
    def dispA(self):
        print("Inside dispA")

class B(A):
    def dispB(self):
        print("Inside dispB")

b = B()
b.dispB()
b.dispA()
