def countfac(n):
    countfact1 = 0
    countfact = 0
    for i in range(1,n+1):
        countfact += 1
        if (n % i == 0 ):
            print(i, end=" ")
            countfact1 += 1
    return countfact
    
n = int(input("Enter the number:"))
print(f"The factors of {n} are:")
res = countfac(n)
print(f"\nThe count of cycle is {res}")
#The number of cycles executed to print minimal number of factors is very high. The above logic is not efficient