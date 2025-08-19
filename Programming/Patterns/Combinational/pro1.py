n = int(input("Enter n:"))
noc = 1
for i in range(1,(n*2)):
    for j in range(1,noc+1):
        print("*",end="")
    if i < n:
        noc +=1
    else:
        noc -=1
    print()

#Opposite of above
noc = 1
for i in range(1,(n*2)):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("*",end="")
    if i < n:
        noc +=1
    else:
        noc -=1
    print()

#Diamond pattern
noc = 1
for i in range(1,(n*2)):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("* ",end="")
    if i < n:
        noc +=1
    else:
        noc -=1
    print()
