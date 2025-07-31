def fun1():
    a = 99
    print("From fun1 a is",a)
    def fun2():
        a = 10
        b = 20
        print("From fun2 b is",b)
        print("From fun2 a is",a)
    fun2()
    print("From fun1 a is",a)
    #print("from fun1 b is",b)
fun1()