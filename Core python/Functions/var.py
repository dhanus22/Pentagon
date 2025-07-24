def fun1():
    print("Inside fun1")
def fun2(a,b):
    c = a + b
    print("the sum is",c)

fun1()
x = 40
y = 50
fun2(x,y)

ptr1 = fun1
ptr2 = fun2
ptr1()
ptr2(10,20)
