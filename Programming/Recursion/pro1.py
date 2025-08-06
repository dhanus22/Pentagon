def printnum(n):
    if (n <= 0):
        return
    print(n,end=" ")
    printnum(n-1)
    print(n,end=" ")

#n = int(input("Enter the number:"))
printnum(4)
