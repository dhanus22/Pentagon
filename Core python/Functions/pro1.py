def fun1():
    print("inside function")
def fun2(a,b):
    c = a + b
    print("sum is: ",c)

def display(ptr1,ptr2):
    ptr1()
    a = 10
    b = 20
    ptr2(a,b)

fun1()
fun2(40,30)

ptr3 = fun1
ptr4 = fun2
x = 5
y = 6
ptr3()
ptr4(x,y)
display(ptr3,ptr4)



