def outer():
    print("Entering outer")
    def inner():
        print("Entering inner")
        print("Processing")
        print("Leaving inner")
    return inner
ref1 = outer()
print("Afte executing outerr")
ref1()
print("AFter executing inner using ref1")