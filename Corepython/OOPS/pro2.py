class Book:
    def __init__(self,values):
        self.__pages = values
    
    def setter(self,values):
        if(values > 0):
            self.__pages = values
    
    def getter(self):
        return self.__pages

b = Book(100)
b.setter(114)
res = b.getter()
print(res)
b.setter(-99)
print(b.getter())