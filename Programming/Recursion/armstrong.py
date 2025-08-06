def countdig(n,count):
    if (n  <= 0):
        return count
    n = n // 10
    count += 1
    return countdig(n,count)

def armstrong(n,pow,asn,temp):
    if (n <= 0):
        return temp == asn
    base = n % 10
    asn = asn + (base**pow)
    n = n // 10
    return armstrong(n,pow,asn,temp)

n = int(input("Enter the number:"))
pow = countdig(n,0)
flag = armstrong(n,pow,0,n)
if flag:
    print(f"{n} is armstrong number")
else:
    print(f"{n} is not armstrong")




