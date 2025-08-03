def prime(n):
    i = 1
    count = 0
    while(i * i <= n):
        if (n % i == 0):
            print(i, end=" ")
            count = count + 1
            if (i != (n // i)):
                print(n // i, end=" ")
                count = count + 1
        i += 1
    return count == 2
n = int(input("Enter the number:"))
flag = prime(n)
if flag:
    print(f"\n{n} is prime")
else:
    print(f"\n{n} is not prime")