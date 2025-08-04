def evenodd(n):
    return (n % 2 == 0)

n = int(input("enter num"))
flag = evenodd(n)#Flag is a standard variable name to hold a Boolean value

if flag:
    print(f"{n} is even")
else:
    print(f"{n} is odd")