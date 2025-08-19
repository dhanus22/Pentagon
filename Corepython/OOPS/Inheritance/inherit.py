class Parent:
    def __init__(self):
        self.a = 10
    
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.b = 20

c = Child()
print(c.b)
print(c.a)
    