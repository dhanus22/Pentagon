def operation(num):
    return num + 10

l = [ ]
i = 0
while(i <= 4):
    print("enter the value")
    data = int(input())
    l.insert(i,data)
    i = i + 1
print(l)

k = list(map(operation,l))
print(k)