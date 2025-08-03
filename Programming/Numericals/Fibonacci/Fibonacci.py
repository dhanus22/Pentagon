def decrewhile(pos):
    n1 = 0
    n2 = 1
    temp = 1
    while(pos > 0):
        print(n1,end=" ")
        temp = n1 + n2
        n1 = n2
        n2 = temp
        pos -= 1

pos = int(input("Enter your position:"))
decrewhile(pos)

