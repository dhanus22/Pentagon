def fun1():
    print("Indside function1")
def fun2():
    print("Inside fun2")

def desplay(ptr1,ptr2):
    print(ptr1)
    print(ptr2)
    ptr1()
    ptr2()

print(fun1)
print(fun2)

ref1 = fun1
ref2 = fun2

print(ref1)
print(ref2)
desplay(ref1,ref2)