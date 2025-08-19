def printfac(n,i):
    if (i > n):
        return
    
    if (n % i == 0):
        print(i,end=" ")
    return printfac(n, i + 1)

n = int(input("Enter n:"))
printfac(n,1)