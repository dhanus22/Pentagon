n = int(input("Enter n:"))
#LHS Right angle triangle
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (i== n or j == 1 or i==j ):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# print("_________________________")

#RHS Right angle triangle
# for i in range(1,n+1):
#     for k in range(n,i,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         if (i== n or j == 1 or i==j ):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# print("_________________________")

#Pyramid
# for i in range(1,n+1):
#     for k in range(n,i,-1):
#         print(" ",end="")
#     for j in range(1,n+1):
#         if (i== n or j == 1 or i==j ):
#                 print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# print("_________________________")

# Inverted LHS Right angle triangle
# for i in range(n,1-1,-1):
#     for j in range(1,n+1):
#         if (i== n or j == 1 or i==j ):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# print("_________________________")

#Inverted RHS Right angle triangle
# for i in range(n,1-1,-1):
#     for k in range(n,i,-1):
#         print(" ",end="")
#     for j in range(1,n+1):
#         if (i== n or j == 1 or i==j ):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# print("_________________________")

#Inverted pyramid
# for i in range(n,(1-1),-1):
#     for k in range(n,i,-1):
#         print(" ",end="")
#     for j in range(1,n+1):
#         if (i== n or j == 1 or i==j ):
#                 print("* ",end="")
#         else:
#             print("  ",end="")
#     print()

#Combinational patterns
# noc = 1
# for i in range(1,(n*2)):
#     for j in range(1,noc+1):
#         if (j == 1 or j == noc):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     if i < n:
#         noc +=1
#     else:
#         noc -=1
#     print()


# noc = 1
# for i in range(1,(n*2)):
#     for k in range(n,noc,-1):
#         print(" ",end="")
#     for j in range(1,noc+1):
#         if (j == 1 or j == noc):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     if i < n:
#         noc +=1
#     else:
#         noc -=1
#     print()

#Diamond 
# noc = 1
# for i in range(1,(n*2)):
#     for k in range(n,noc,-1):
#         print(" ",end="")
#     for j in range(1,noc+1):
#         if (j == 1 or j == noc):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     if i < n:
#         noc +=1
#     else:
#         noc -=1
#     print()

#K pattern
noc = n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ", end=" ")
    for j in range(1,(noc+1)):
        if ( i == 1 or i == (n *2)-1 or j == 1 or j == noc):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i < n:
        noc -=1
    else:
        noc +=1

