l = [ ]
i = 0
while(i <= 4):
    print("enter the value")
    data = int(input())
    l.insert(i,data)
    i = i + 1
print(l)

k = list(map(lambda data:(data + 10),l))
print(k)