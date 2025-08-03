#program to print first n prime numbers
def isprime(n):
    i = 1
    count = 0
    while(i * i <= n):
        if (n % i == 0):
            count = count + 1
            if(i != (n//i)):
                count = count + 1
        i = i + 1
    return count == 2

count = int(input("Enter the number:"))
num = 2
while count > 0:
    if isprime(num):
        print(num,end=" ")
        count -= 1
    num += 1

    


