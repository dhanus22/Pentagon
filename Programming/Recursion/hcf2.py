def gcd(n1,n2):
    if n1 <= 0:
        return n2
    if (n2 > n1):
        n1, n2 = n2, n1
    #return gcd((n1 - n2), n2)
    return gcd((n1 % n2), n2)

n1 = int(input("Enter n1:"))
n2 = int(input("enter n2:"))
res = gcd(n1,n2)
print(f"The hcf of {n1} and {n2} is :{res}")
