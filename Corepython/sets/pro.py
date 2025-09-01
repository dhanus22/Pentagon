s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {5, 6, 7, 8}
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s3))
print(s3.isdisjoint(s1))

s1 = {1, 2, 3}
s2 = {1, 2}
print(s1.issuperset(s2))
print(s2.issuperset(s1))
print(s1.issubset(s2))
print(s2.issubset(s1))

a1 = {12, 23, 45, 56, 67}
set1 = frozenset([10, 20, 30, 40, 50])
print(set1)
set1.add(60)
set1.discard(30)

s1 = {10,20,30,[40,50]}
print(s1)

s2 = {10,20,30,(40,50)}
print(s2)

s3 = {10,20,30,[40,50,60]}
print(s3)