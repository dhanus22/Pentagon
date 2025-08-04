def evenodd(n):
    return n % 2 == 0

sr = int(input("enter start range"))
er = int(input("Enter end value"))
if (sr > er):
    print("invalid input")
else:
    for i in range(sr,er+1):
        flag = evenodd(i)
        if flag:
            print(i, end=" ")
    
    print("\n Odd numbers:")
    for i in range(sr,er+1):
        flag = evenodd(i)
        if not flag:
            print(i, end=" ")
