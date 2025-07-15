n = int(input("enter a number"))
if(n == 0):
    print("neutral")
else:
    if (n % 2 == 0):
        if(n > 0):
            print("Positive even number")
        else:
            print("negative even num")
    else:
        if(n < 0):
            print("negative odd number")
        else:
            print("positive odd number")

 