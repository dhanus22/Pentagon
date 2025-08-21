n = int(input("Enter n:"))

# K pattern
noc = n  
for i in range(1, n * 2):
    for j in range(noc):
        print("*", end=" ")
    print()
    
    if i < n:
        noc -= 1   
    else:
        noc += 1   

print("____________________________")

# #X pattern
noc = n  
for i in range(1, n * 2):
    for k in range(n, noc, -1):
        print(" ", end="")
    for j in range(noc):
        print("*", end=" ")
    print()
    
    if i < n:
        noc -= 1   
    else:
        noc += 1   

print("____________________________")

#inverted K pattern
noc = n  
for i in range(1, n * 2):
    for k in range(n,noc,-1):
        print(" ", end=" ")
    for j in range(noc):
        print("*", end=" ")
    print()
    
    if i < n:
        noc -= 1   
    else:
        noc += 1 