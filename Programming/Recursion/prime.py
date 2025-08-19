def isprime(n,i,count):
    if (i * i > n):
        return count == 2

    if (n % i == 0):
        count +=1
        if (i != (n//i)):
            count += 1
    
    return isprime(n,(i + 1),count)

n = int(input("Enter n:"))
flag = isprime(n,1,0)
if flag:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")

