def printnum(n):
    if (n <= 0):
        return
    print(n,end=" ")
    printnum(n-1)
    print(n,end=" ")

def display(i,n):
    if (i > n):
        return
    print(i, end=" ")
    display((i+1),n)
    print(i, end=" ")
    
n = int(input("Enter the number:"))
printnum(n)
print("\n_________________")
display(1,n)
