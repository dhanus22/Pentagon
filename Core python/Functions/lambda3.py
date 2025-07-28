def even(num):
    if(num % 2 == 0):
        return True
    else:
        return False
    
l = [ ]
i = 0
while(i <= 4):
    print("enter the value")
    data = int(input())
    l.insert(i,data)
    i = i+1
print(l)

i = 0
while(i <= 4):
    ext = l[i]
    status = even(ext)
    if(status == True):
        print(l[i])
    i = i+1

