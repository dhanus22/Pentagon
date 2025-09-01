#print(len(10))#error single valueddata is not allowed
# l1 = [1,3,"abc",23]
# print(len(l1))
# l1 = []
# print(l1)
# t1 = (1, 2, 3, 3, 3)
# print(t1)
# a1 = "djdksjdsj"
# print(len(a1))
# set1 = {1, 2, 3, 3, 4}
# print(len(set1))
# dict = {101: "ramu", 102: "SITa"}
# print(len(dict))
l1 = []
#l1[0] = 199 #index eror
# l1.append(22)
# l1.append(22.7)
# l1.append("abc")
# l1.append([100,200])
# l1[0] = 3
# print(l1)

l1.insert(2,333)
l1.insert(99,444)
l1.insert(100,[555])
l2 = [22,32,42]
l3 = [45,65]
l2.extend(l3) #l2 is calling list, l3 is argument list
s1 = "ab"
l2.extend(s1)
#l2.extend(301)
print(l1)
print(l2)
print(l3)

