def evenodd(n):
    return n % 2 == 0

count = int(input("enter the count of even num to be printed"))

series = 1
while count > 0:
    flag = evenodd(series)
    if flag:
        print(series, end=" ")
        count -= 1
    series += 1