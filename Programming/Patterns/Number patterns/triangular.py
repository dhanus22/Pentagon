n = int(input("Enter n:"))
# for i in range(1,(n+1)):
#     for j in range(1,(i+1)):
#         if ((i + j) % 2 == 0):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()
# # Enter n:4
# # 1 
# # 0 1
# # 1 0 1
# # 0 1 0 1

# for i in range(1,(n+1)):
#     for j in range(1,(n+1)):
#         if ((i + j) % 2 == 0):
#             print("0",end=" ")
#         else:
#             print("1",end=" ")
#     print()

# # Enter n:4
# # 0 1 0 1 
# # 1 0 1 0
# # 0 1 0 1
# # 1 0 1 0

temp = 1
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        print(temp,end=" ")
        temp = temp + 1
    print()
# # Enter n:4
# # 1 2 3 4 
# # 5 6 7 8
# # 9 10 11 12
# # 13 14 15 16

tempincre = 1
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if (i % 2 != 0):
            print(tempincre,end=" ")
            tempdecre = tempincre
        else:
            print(tempdecre,end=" ")
            tempdecre = tempdecre - 1
        tempincre = tempincre + 1
    print()
# # Enter n:4
# # 1 2 3 4 
# # 4 3 2 1
# # 9 10 11 12
# # 12 11 10 9

tempincre = 1
for i in range(1,(n+1)):
    for j in range(1,(i+1)):
        if (i % 2 != 0):
            print(tempincre,end=" ")
            tempdecre = tempincre
        else:
            print(tempdecre,end=" ")
            tempdecre = tempdecre - 1
        tempincre = tempincre + 1
    print()
    tempdecre = tempincre + i
# Enter n:4
# 1 
# 3 2
# 4 5 6
# 10 9 8 7