def outer():
    print("Inside outer")
    def inner():
        print("Inside inner")
    return inner
ref1 = outer()
print(ref1)
ref1()