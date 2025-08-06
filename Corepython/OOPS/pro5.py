#propertydecorator 
class Student:
    def __init__(self):
        self.__name = " "
    
    @property
    def dataAccess(self):
        return self.__name
    
    @dataAccess.setter
    def dataAccess(self,value):
        self.__name = value

s = Student()
s.dataAccess ="rama"
res = s.dataAccess
print(res)
