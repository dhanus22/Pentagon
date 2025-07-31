n = int(input("Enter the number"))
temp = n
rev = 0
if (n < 0):
    n = n * -1
while(n > 0):
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10

if (temp < 0):
    rev = rev * -1
print(f"the reversal of {n} is {rev}")
