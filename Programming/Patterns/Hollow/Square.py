n = int(input("Enter n:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("_________________________________________")
print()
if n % 2 == 0:
    n += 1
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i == 1 or i == n or j == 1 or j == n or i==j or (i+j == n+1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("_________________________________________")
print()
if n % 2 == 0:
    n += 1
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i == 1 or i == n or i==j or (i+j == n+1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("_________________________________________")

print()
if n % 2 == 0:
    n += 1
for i in range(1,n+1):
    for j in range(1,n+1):
        if (j == 1 or j == n or i==j or (i+j == n+1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()