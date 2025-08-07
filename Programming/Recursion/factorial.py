def factorial(n,i):
    if (i * i >= n):
        return 
    if ((n % i) == 0):
        print(i,end=" ")
        if (i != (n // i)):
            print((n // i),end=" ")
    i = i + 1
    return factorial(n,i)

n = int(input("Enter n:"))
factorial(n,1)

    