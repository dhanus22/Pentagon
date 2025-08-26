#Zip function
from itertools import zip_longest

names = ["Kohli","Rohit","Rahul","Manish"]
runs = [1000,9000,8000,7000]
country = ["IND","IND","IND","IND"]
ipl_t = ["RCB","MI","DC","KKR"]
info = list(zip(names,runs,country,ipl_t))
print(info)

names = ["Kohli","Rohit","Rahul","Manish"]
runs = [1000,9000,8000,7000]
country = ["IND","IND","IND","IND"]
ipl_t = ["RCB","MI"]
info1 = list(zip_longest(names,runs,country,ipl_t,fillvalue="#"))
print(info1)
