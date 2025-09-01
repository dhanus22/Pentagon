#Write a program to find to find the number in given array using linear search
def createarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a num: "))
            l1.append(n)
        except Exception as e:
            return l1
        
print("enter values into an array")
arr=createarray()
target=int(input("enter a target element to be searched: "))
flag, index= False, -1
for i in range(0, len(arr)):
    if target==arr[i]:
        flag=True
        index=i
        break

if flag:
    print(f"the {target} element is found at:{index}")
else:
    print(f"the {target} element is not found")


#Using function
def createarr():
    l1 = []
    while True:
        try:
            n = int(input("Enter n: "))
            l1.append(n)
        except Exception as e:
            return l1

def linearsearch(arr,target):
    for i in range(0, len(arr)):
        if target == arr[i]:
            return True,i
    return False, i

print("Enter the values into the array:")
arr = createarr()
target = int(input("Enter the number to be searched"))
flag, index = linearsearch(arr,target)
if flag:
    print(f"{target} found at index {index}")
else:
    print(f"{target} not found")




#Maximum number of the given array
def creatarr():
    l1 = []
    while True:
        try:
            n = int(input("ENter num:"))
            l1.append(n)
        except Exception as e:
            return l1


def findmax(arr):
    max = (-2**31)-1
    maxind = -1
    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
            maxind = i
    return max, maxind

arr = creatarr()
max, maxind = findmax(arr)
print(f"The largest is {max} found at {maxind}")


#Minimum of given array

def findmin(arr):
    min = (2**31)
    minind = -1
    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]
            minind = i
    return min, minind

arr = creatarr()
min, minind = findmin(arr)
print(f"The smallest is {min} found at {minind}")

    
