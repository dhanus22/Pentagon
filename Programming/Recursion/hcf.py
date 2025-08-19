def gcd(n1,n2,i,hcf,lower):
    if (i > lower):
        return hcf

    if(n1 % i == 0 and n2 % i == 0):
        hcf = i
    return gcd(n1,n2,i+1,hcf,lower)
 
n1 = int(input("Enter n1:"))
n2 = int(input("enter n2:"))
lower = n1
if (n2 > n1):
    lower = n2
res = gcd(n1,n2,2,1,lower)
print(f"The hcf of {n1} and {n2} is :{res}")




