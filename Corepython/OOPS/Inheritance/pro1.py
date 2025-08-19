class Animal:
    def eat(self):
        print("A is eating")
    def sleep(self):
        print("A is sleeping")
    def Breath(self):
        print("A is breating")

class Tiger(Animal):
    pass

class Deer(Animal):
    pass

class Monkey(Animal):
    pass

t = Tiger()
d = Deer()
m = Monkey()
d.eat()
d.sleep()
d.Breath()
t.eat()
t.sleep()
t.Breath()
m.eat()
m.sleep()
m.Breath()
