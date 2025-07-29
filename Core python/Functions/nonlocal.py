def fun1():
    a = 99
    b = 23
    print("From fun1 a is",a)
    print("From fun1 b is",b)
    def fun2():
        nonlocal a,b
        a = 10
        b = 20
        print("From fun2 b is",b)
        print("From fun2 a is",a)
    fun2()
    print("From fun1 a is",a)
    #print("from fun1 b is",b)
fun1()