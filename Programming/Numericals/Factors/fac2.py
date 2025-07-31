def factors(n):
    for i in range(1,n+1):
        if(n % i == 0):
            print(i,end=" ")

sr = int(input("Enter start range:"))
er = int(input("Ente end range:"))
if (sr > er):
    print("Invalid input")


