class Book:
    def __init__(self, value):
        self.__pages = value

b = Book(100)
print(b.__pages)
