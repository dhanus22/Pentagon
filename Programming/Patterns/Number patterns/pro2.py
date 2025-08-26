n = int(input("Enter n:"))
# noc = n
# for i in range(1,(n*2)):
#     for j in range(1,noc+1):
#         print(j,end="")
#     print()
#     if i < n:
#         noc -= 1
#     else: 
#         noc +=1
#O/P
# Enter n:4
# 1234
# 123
# 12
# 1
# 12
# 123
# 1234

# noc = n
# for i in range(1,(n*2)):
#     for j in range(noc,0,-1):
#         print(j,end="")
#     print()
#     if i < n:
#         noc -= 1
#     else:
#         noc +=1
#O/P
# Enter n:4
# 4321
# 321
# 21
# 1
# 21
# 321
# 4321

# noc = n
# for i in range(1,(n*2)):
#     for k in range(n,noc,-1):
#         print(" ",end="")
#     for j in range(noc,0,-1):
#         print(j,end="")
#     print()
#     if i < n:
#         noc -= 1
#     else:
#         noc +=1
# Enter n:4
# 4321
#  321
#   21
#    1
#   21
#  321
# 4321

for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if (i < j):
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
# Enter n:4
# 1 1 1 1 
# 1 2 2 2
# 1 2 3 3
# 1 2 3 4


for i in range(n,(1-1),-1):
    for j in range(n,(1-1),-1):
        if (i > j):
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()
# Enter n:4
# 4 3 2 1 
# 3 3 2 1
# 2 2 2 1
# 1 1 1 1

for i in range(1,(n+1)): 
    for j in range(1,(n+1)):
        if(j > i):
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()

# Enter n:5
# 1 2 3 4 5 
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5




if (n % 2 == 0):
    n = n + 1
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if (i == j or (i+j == n+1)):
            print(i,end=" ")
        else:
            print("*",end=" ")
    print()
# Enter n:4
# 1 * * * 1 
# * 2 * 2 *
# * * 3 * *
# * 4 * 4 *
# 5 * * * 5

if (n % 2 == 0):
    n = n + 1
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if (i == j or (i+j == n+1)):
            print(j,end=" ")
        else:
            print("*",end=" ")
    print()
# Enter n:4
# 1 * * * 5 
# * 2 * 4 *
# * * 3 * *
# * 2 * 4 *
# 1 * * * 5

    
    
    
