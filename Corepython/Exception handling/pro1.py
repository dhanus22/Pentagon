# def fun1():
#     print("entering fun1")
#     try:
#         fun2()
#     except Exception as e:
#         print("error in fun1")
#     print("Leaving fun1")

# def fun2():
#     print("Entering fun2")
#     res = 10/0
#     print(res)
#     print("Leaving fun2")

# print("Program started")
# fun1()
# print("Program Ended")




#Rethrowing an error
def fun1():
    print("entering fun1")
    try:
        fun2()
    except Exception as e:
        print("error in fun1")
    print("Leaving fun1")

def fun2():
    print("Entering fun2")
    try:
        res = 10/0
        print(res)
    except Exception as e:
        print("error in fun2")
    print("Leaving fun2")
    raise e #works with return


print("Program started")
fun1()
print("Program Ended")
