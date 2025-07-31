#Print the list of integers from  through  as a string, without spaces.
if __name__ == '__main__':
    n = int(input())
    a = 1
    for i in range(a,n+1):
        print(i, end='')  # Print without spaces