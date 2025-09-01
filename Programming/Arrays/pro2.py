ele = input("Enter val:")
print(ele)
print(type(ele))
print("============================")
try:
    ele = int(input("Enter val:"))
    print(ele)
    print(type(ele))
except Exception as e:
    print("Invalid I/O")

#Write a program to create a dynamic integer array with user define values
def creatarr():
    l1 = []
    while True:
        try:
            n = int(input("enter num:"))
            l1.append(n)
        except Exception as e:
            return l1

arr = creatarr()
print(arr)

#Write a program to create a dynamic character array with user define values
def stringarray():
    l1 = []
    while True:
        try:
            n = input("enter char:")
            if n == "":
                return l1
            l1.append(n)
        except Exception as e:
            return l1

arr = stringarray()
print(arr)

def chararray():
    l1 = []
    while True:
        n = input("enter char:")
        if n == "":
            return l1
        l1.append(n[0])

arr = chararray()
print(arr)

