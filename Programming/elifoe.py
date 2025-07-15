#odd or even with elif
n = int(input("enter a number"))
if(n > 0 and n%2 == 0):
    print(f"{n} is positive even number")
elif(n > 0 and n%2 != 0):
    print(f"{n} is positive odd number")
elif(n < 0 and n%2 == 0):
    print(f"{n} is negative even number")
elif(n < 0 and n%2 != 0):
    print(f"{n} is negative odd number")
else:
    print("neutral")