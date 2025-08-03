def outer():
    print("Entering outer")
    def inner():
        print("Entering inner")
        print("Processing ")
        print("Leaving inner")
    inner()
outer()
print("Program ended")