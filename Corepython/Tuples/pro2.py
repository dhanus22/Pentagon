a = (10,20,30,40,50)
b = a[0:2] + (25,) + a[2:]
print(b)

#Deletiion
c = a[0:2] + a[3:]
print(c)

studentinfo = ("Rama",[40,50,60])
name,marks = studentinfo
print(name) 
print(marks)

#Nested tuple
a = (10,20,30,("Python","Java",(99.8,88.4)),40,50,60)
print(a)
print(len(a))
print(a[6])
print(a[3][0])
print(a[3][2][1])
print(a[3][2])