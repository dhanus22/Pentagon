def faccount(n,i,count):
    if (i > n):
        return count
    
    if (n % i == 0):
        count += 1
    
    return faccount(n,i+1,count)

n = int(input("Enter n:"))
res = faccount(n,1,0)
print(f"The factor count of {n} is:{res}")
