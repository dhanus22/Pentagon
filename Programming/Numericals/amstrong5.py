#first n armstrong numbers
def countdig(n):
    count = 0
    while (n > 0):
          n = n // 10
          count = count + 1
    return count

def armstrong(n):
      temp = n
      asn = 0
      if (n < 0):
          n = n * -1
      pow = countdig(n)
      while( n > 0):
            rem = n % 10 #get last digit
            asn = asn + (rem ** pow) #sum up the power of digits
            n = n // 10 #remove digit
      if(temp < 0):
            asn = asn * -1 
      if (temp == asn):
            return True
      else:
            return False
      
n = int(input("enter number:"))
print("Armstrong numbers :")
for i in range(n):
      flag = armstrong(i)
      if flag:
             print(i, end=" ")


          
    



