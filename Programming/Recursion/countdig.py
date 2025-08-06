def countdig(n,count):
    if (n  <= 0):
        return count
    n = n // 10
    count += 1
    return countdig(n,count)

n = int(input("Enter the number:"))
res = countdig(n,0)
print(f"The count of dig  {n} is:{res}")