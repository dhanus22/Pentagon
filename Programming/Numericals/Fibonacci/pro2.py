#Incrementing for loop
def increfor(pos):
    n1 = 0
    n2 = 1
    temp = 1
    for i in range(pos):
        print(n1, end=" ")
        temp = n1 + n2
        n1 = n2
        n2 = temp

pos = int(input("Enter your position:"))
increfor(pos)