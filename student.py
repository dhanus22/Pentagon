class Student:
    def __init__(self):
        self.name = "rama"
        self.age = 23
        self.quali = "BE"
        self.add = "Bang"

    def eat(self):
        print("Stud is eating")

    def study(self):
        print("Stud is studying")

s1 = Student()
print(s1.name)
print(s1.age)
print(s1.quali)
print(s1.add)

s1.eat()
s1.study()