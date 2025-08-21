a = [10,20,30,40]
print(a)
a1 = a #shallow copy
print(a)
a[2] = 60
print(a)
print(a1)

b = a.copy() #Deep copy
a[2] = 30
print(a)
print(a1)
print(b)

