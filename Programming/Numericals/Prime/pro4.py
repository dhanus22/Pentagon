def printnum4(n):
    print(n)
    printnum3(n-1)

def printnum3(n):
    print(n)
    printnum2(n-1)

def printnum2(n):
    print(n)
    printnum(n-1)

def printnum(n):
    print(n)

printnum4(4)