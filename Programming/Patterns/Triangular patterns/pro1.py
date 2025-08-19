#Square
n = int(input("Enter n:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()

#LHS right angle triangle
n = int(input("Enter n:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

