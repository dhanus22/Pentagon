#Reversal of a number
def reversal(n,rev):
    if (n <= 0):
        return rev

    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10

    return reversal(n,rev)

n = int(input("Enter n:"))
res = reversal(n,0)
print(f"The reversal of {n} is:{res}")