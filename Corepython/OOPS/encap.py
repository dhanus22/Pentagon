class Book:
    def __init__(self, value):
        self.pages = value

b = Book(100)
print(b.pages)
b.pages = 114
print(b.pages)
b.pages = -99
print(b.pages) 