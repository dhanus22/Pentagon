#break: It is keyword to exit the current executing loop
while True:
    n = int(input("enter n:"))
    if (n == 5):
        break
    elif (n ==3 or n == 10):
        continue #keyword to skip a cycle in the current executing loop without exiting the loop
print("program executed")
