def print_msg():
    print("Hello everyone")
def outer(print1):
    print("Entering outer")
    def inner():
        print("Entering inner")
        ref1 = print1
        ref1()
        print("Leaving inner")
    return inner
ptr1 = print_msg
ptr2 = outer(ptr1)
print("After executing outer")
ptr2()
print("Afetr executing inner using ptr2")
