def fibonacci(pos,n1,n2):
    if (pos <= 0):
        return 
    print(n1,end=" ")
    temp = n1 + n2
    #n1 = n2
    #n2 = temp
    return fibonacci(pos-1,n1 = n2,n2 = temp)

pos = int(input("enter your position:"))
fibonacci(pos,0,1)

