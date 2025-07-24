def fun(): #no parameters no return value
    a = 10
    b = 20
    c = a + b
    print(c)

def fun2(): #no parameters with return value
    a = 10
    b = 20
    c = a + b
    return c

def fun3(a,b): #parameters without return value
    c = a + b
    print(c)

def fun4(a,b): #with parameters and return value
    c = a + b
    return c

fun()
r1 = fun2()
print(r1)
x = 10
y = 20
fun3(x,y)
r2 = fun4(x,y)
print(r2)
