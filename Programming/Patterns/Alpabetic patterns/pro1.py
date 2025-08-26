# print(ord("A"))
# print(ord(" "))
# print(ord("a"))
# #print(ord("")) --- Error
# #print(ord("ab")) --- Error
# print("_____________________________")
# print(chr(122))
# print(chr(0))
# print(chr(2222))
#print(chr(-22)) --- Error

n = int(input("Enter n:"))

# for i in range(1,(n+1)):
#     for j in range(1,(i+1)):
#         print(chr(96+i),end="")
#     print()
# Enter n:4
# a
# bb
# ccc
# dddd

# for i in range(n,(1-1),-1):
#     for j in range(1,(i+1)):
#         print(chr(64+j),end="")
#     print()

# Enter n:4
# ABCD
# ABC
# AB
# A

# for i in range(1,(n+1)):
#     for j in range(1,(n+1)):
#         if (i % 2 != 0):
#             print(chr(64+j),end="")
#         else:
#             print(chr(96+j),end="")
#     print()  
# Enter n:4
# ABCD
# abcd
# ABCD
# abcd

# for i in range(n,(1-1),-1):
#     for j in range(1,(i+1)):
#         if (j % 2 == 0):
#             print(chr(64+j),end="")
#         else:
#             print(chr(96+j),end="")
#     print()
# Enter n:4
# aBcD
# aBc
# aB
# a

# for i in range(1,(n+1)): #Correction
#     for j in range(1,(n+1)):
#         if (i == j) or (i+j % 2 == 0):
#             print(chr(64+j),end="")
#         else:
#             print(chr(96+j),end="")
#     print()

# Enter n:4
# Abcd
# aBcd
# abCd
# abcD

temp = 1 
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if(temp % 2 != 0):
            print(chr(64+temp),end="")
        else:
            print(chr(96+temp),end="")
        temp = temp +1
    print()

# Enter n:4
# AbCd
# EfGh
# IjKl
# MnOp

# noc = 1
# for i in range(1,(n*2)):
#     for j in range(noc,(n+1)):
#         print(chr(96+j),end="")
#     print()
#     if i < n:
#         noc += 1
#     else:
#         noc -= 1
# abcd
# bcd
# cd
# d
# cd
# bcd
# abcd