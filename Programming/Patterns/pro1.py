n = 4


for i in range(1,(n+1)):
    for j in range(1,(i+1)):
        print("*",end="")
    print()

print("___________________________________")

for i in range(1,(n+1)):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,(i+1)):
        print("*",end="")
    print()

print("___________________________________")

for i in range(n,1-1,-1):
    for j in range(1,(i+1)):
        print("*",end="")
    print()

print("___________________________________")

for i in range(n,(1-1),-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,(i+1)):
        print("*",end="")
    print()

print("___________________________________")

for i in range(1,(n+1)):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,(i+1)):
        print("* ",end="")
    print()

print("___________________________________")

for i in range(n,(1-1),-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,(i+1)):
        print("* ",end="")
    print()

print("___________________________________")

odd = 1
for i in range(1,(n+1)):
    for j in range(1,(odd+1)):
        print("*",end="")
    odd = odd + 2
    print()

# Combinational patterns

noc = 1
for i in range(1,(n*2)):
    for j in range(1,(noc+1)):
        print("*",end="")
    if (i < n):
        noc += 1
    else:
        noc -= 1
    print()

print("___________________________________")

noc = 1
for i in range(1,(n*2)):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,(noc+1)):
        print("*",end="")
    if (i < n):
        noc += 1
    else:
        noc -= 1
    print()
print("___________________________________")

noc = 1
for i in range(1,(n*2)):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,(noc+1)):
        print("* ",end="")
    if (i < n):
        noc += 1
    else:
        noc -= 1
    print()

print("___________________________________")

noc = 1
nor = (n*2)-1
for i in range(1,2*n):
    for j in range(1,2*n):
        if (j <= noc) or (j >= nor):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    if (i < n):
            noc += 1
            nor -= 1
    else:
        noc -= 1
        nor += 1
    print()

