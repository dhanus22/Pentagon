# a = [10,20,30,40,50]
# print(a)
# a.insert(2,25)
# print(a)
# a.append(60)
# a.append(70)
# a.append(80)
# #a.append(90,100,110)

# b = [90,100,110]
# a.extend(b)
# a.extend([120,130,140])
# print(a)


# a = [10,20,30,40,50,60,70]
# print(a)
# a.remove(30)
# print(a)
# a.pop()
# a.pop()
# print(a)

# a.pop(1)
# print(a.count(10))
# print(a.index(50))
# a.clear()
# print(a)
# del a
# print(a)

a = [10,20,30,40,50]
print(a)
for i in a:
    print(i)

for index,data in enumerate(a):
    print(index," ",data)

#range function in list
a = list(range(10))
b = list(range(15,25,2))
c = list(range(15,25,2))

print(a)
print(b)
print(c)

