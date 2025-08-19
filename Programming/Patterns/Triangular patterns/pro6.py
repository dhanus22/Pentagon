# Triangular patterns

#Inverted pyramid
n = int(input("Enter n:"))
for i in range(n,1-1,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()

#Odd right angle triangle
odd = 1
for i in range(1,n+1):
    for j in range(1,odd+1):
        print("*",end="")
    odd = odd + 2
    print()

#Using explicit spacing
odd = 1
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,odd+1):
        print("*",end="")
    odd = odd + 2
    print()

#Inverted odd pyramid
odd = (n * 2) - 1
for i in range(n,1-1,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,odd+1):
        print("*",end="")
    odd = odd - 2
    print()

#In straight triangles the order of i and j will be same
#In inverted triangles the order of i and j will be opposite