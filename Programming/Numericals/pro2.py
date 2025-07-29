def countdig(n):
      if (n < 0):
          n = n * -1
      count = 0
      while (n > 0):
          n = n // 10
          count = count + 1
      return count
    
n = int(input("enter num:"))
res = countdig(n)
print(f"The count of digit in {n} is: {res}")

