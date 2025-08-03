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
      
sr = int(input("enter the start value"))
er = int(input("enter the end value"))
if (sr > er):
    print("invalid input")
    
print("Armstrong numbers :")
for i in range(sr, er + 1):
      flag = armstrong(i)
      if flag:
            print(i, end=" ")


          
    


