a = []
i = 0

while(True):
    print("Enter the value:")
    data = int(input())
    a.insert(i,data)
    i += 1
    print("Do you wish to continue Press 1 = Yes Press 2 = No")
    choice = int(input())
    if(choice == 1):
        continue
    else:
        break

print(a)