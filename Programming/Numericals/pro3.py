def countdig(n):
    count = 0  
    if n == 0:
        return 1
    if n < 0:
        n = -n
    while n > 0:
        n = n // 10
        count = count + 1
    return count

sr = int(input("Enter start range: "))
er = int(input("Enter end range: "))
if sr > er:
    print("Invalid input")
else:
    for i in range(sr, er + 1):
        res = countdig(i)
        print(f"The count of digits in {i} is: {res}")
