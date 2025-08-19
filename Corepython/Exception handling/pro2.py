#Handling specific exception
try:
    print("Enter value 1:")
    a = int(input())
    print("Enter value 2:")
    b = int(input())
    res = a /b
    print(res)
except ValueError as e:
    print("It is VE")
except ZeroDivisionError as e:
    print("It is ZDE")
except Exception as e:
    print("It is an error")

    
