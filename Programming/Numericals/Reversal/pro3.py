def reversal(n):
    temp = n
    rev = 0
    if (n < 0):
        n = n * -1
    while(n > 0):
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10
    
    if (temp < 0):
        rev = rev * -1  
    return rev

sr = int(input("Enter the start range:"))
er = int(input("Enter the end range:"))
if(sr > er):
    print("Invalid input")
for i in range(sr,er+1):
    res = reversal(i)
    print(f"The reversal of {i} is {res} ")





