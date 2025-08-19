def fun1():
    print("Fun1 connected to DB")
    try:
        fun2()
    except Exception as e:
        print("Error in fun1")
        raise e
    finally:
        print("Fun1 closing DB")

def fun2():
    print("Fun2 connected to DB")
    try:
        res = 10/0
        print(res)
    except Exception as e:
        print("Error in fun2")
        raise e
    finally:
        print("Fun2 closing DB")

print("Program started")
try:
    fun1()
except Exception as e:
    print("Error is main")
print("Program ended")
