n = int(input("enter n:"))
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        print(i,end=" ")
    print()
# enter n:4
# 1 1 1 1 
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

for i in range(n,(1-1),-1):
    for j in range(n,(i-1),-1):
        print(i,end=" ")
    print()

#O/p
# enter n:4
# 1 1 1 1 
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

# 4
# 3 3
# 2 2 2
# 1 1 1 1

for i in range(1,n+1):
    for j in range(n,(i-1),-1):
        print(j,end=" ")
    print()
# enter n:4
# 4 3 2 1 
# 4 3 2
# 4 3
# 4

for i in range(n,(1-1),-1):
    for j in range(n,(1-1),-1):
        print(i,end=" ")
    print()
#O/p
# 4 4 4 4
# 3 3 3 3
# 2 2 2 2
# 1 1 1 1

for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(i,(n+1)):
        print(j,end="")
    print()
#O/P
# enter n:4
# 1234
#  234
#   34
#    4

for i in range(1,(n+1)):
    for j in range(i,(n+i)):
        print(j,end="")
    print()

# enter n:4
# 1234
# 2345
# 3456
# 4567
