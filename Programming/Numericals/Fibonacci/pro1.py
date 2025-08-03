#Incrementing while
def increwhile(pos):
    n1 = 0
    n2 = 1
    temp = 1
    i = 0
    while(pos > i):
        print(n1,end=" ")
        temp = n1 + n2
        n1 = n2
        n2 = temp
        i += 1

pos = int(input("Enter your position:"))
increwhile(pos)

