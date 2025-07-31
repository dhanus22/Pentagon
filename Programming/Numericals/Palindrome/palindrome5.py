#program to print first n non-palindromic numbers
def palindrome(n):
    temp = n
    rev = 0
    if(temp < 0):
        n = n * -1
    while(n > 0):
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10
    
    if(temp < 0):
        rev = rev * -1
    
    return (temp == rev)

count = int(input("Enter the number:"))
num = 1
while (count > 0):
    flag = palindrome(num)
    if not flag:
        print(num,end=" ")
        count -= 1
    num += 1 
    
