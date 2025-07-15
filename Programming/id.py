a = 100
b = 100
c = 100
d = a
print(a == b == c == d)
#same shared memory
print(a is d)
print(b is c)
print(a is c)
print("___________________________________")

#same variable different memory
x = 10
print(x)
print(id(x))
x = 20
print(x)
print(id(x))
x = 30
print(x)
print(id(x))
s1 ="abbc123"
print("a" in s1)
print("bbc" in s1)
print("12 in s1")
print("_______________________________________________")
a = 10
#print(1 in a) #error It id sungle valued data #error
 
a = 10
#print("1"in a) #error 

#a = " "
#print("ab" in a)


