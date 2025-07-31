#accessing the global variable and modifying the value
a = 999
def fun1():
    global a
    a = 88
    b = 77
    print(a)
    print(b)

def fun2():
    global a
    a = 66
    c = 55
    print(a)
    print(c)
print(a)
fun1()
fun2()
print(a)
