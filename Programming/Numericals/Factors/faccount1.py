def countfactors(n):
    i = 1
    count = 0
    cyccount = 0
    while(i * i <= n):
        if (n % i == 0):
            print(i, end=" ")
            count = count + 1
            if (i != (n // i)):
                print(n // i, end=" ")
                count = count + 1
        i += 1
    cyccount += 1
    return cyccount,count

n = int(input("Enter the number:"))
res1,res2 = countfactors(n)
print(f"The count {n} of  is {res2}")
print(f"\nThe countcycle of  is {res1}")



               
