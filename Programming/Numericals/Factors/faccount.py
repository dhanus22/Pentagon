def factors(n):
    for i in range(1,n+1):
        if(n % i == 0):
            print(i,end=" ")
def countfac(n):
    countfact = 0
    for i in range(1,n+1):
        if (n % i == 0):
            countfact += 1
    return countfact
    
n = int(input("Enter the number:"))
print(f"The factors of {n} are:")
factors(n)
res = countfac(n)
print(f"\nThe count of {n} is {res}")
