def countfac(n,i,count):
    if (i * i > n):
        return count

    if (n % i == 0):
        count +=1
        if (i != (n//i)):
            count += 1
    
    return countfac(n,(i + 1),count)

n = int(input("Enter n:"))
res = countfac(n,1,0)
print(f"the count of{n} is: {res}")
