#program to print the prime numbers of user defined range
def primerange(n):
    i = 1
    count = 0
    while(i * i <= n):
        if (n % i == 0):
            count = count + 1
            if (i != (n // i)):
                count = count + 1
        i += 1
    return count == 2
sr = int(input("Enter the start range:"))
er = int(input("Enter the end range:"))
primes = []
for i in range(sr, er + 1):
    flag = primerange(i)
    if flag:
        primes.append(i)
if primes:
    print(f"The prime numbers from {sr} to {er} are:", *primes)


    
