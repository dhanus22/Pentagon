def factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
            count += 1
    return count

sr = int(input("Enter start range:"))
er = int(input("Ente end range:"))
if (sr > er):
    print("Invalid input")
for i in range(sr, er + 1):
    print(f"\nFactors of {i} are: ", end="")
    res = factors(i)
    print(f"\nThe count is : {res}")

    

