def countdig(n):
    count = 0
    while (n > 0):
          n = n // 10
          count = count + 1
    return count

n = int(input("enter number:"))
temp = n
if (n < 0):
          n = n * -1
pow = countdig(n)
asn = 0
while( n > 0):
    rem = n % 10 #get last digit
    asn = asn + (rem ** pow) #sum up the power of digits
    n = n // 10 #remove digit
if (temp == asn):
      print(f"{temp} is an Armstrong number")
else:
      print(f"{temp} is not an Armstrong number")
