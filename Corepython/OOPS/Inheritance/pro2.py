class Animal:
    def eat(self):
        print("A is eating")
    def sleep(self):
        print("A is sleeping")
    def Breath(self):
        print("A is breating")

class Tiger(Animal):
    def eat(self):
        print("Tiger will hunt and eat")

class Deer(Animal):
    def eat(self):
        print("Deer will graze and eat")

class Monkey(Animal):
    def eat(self):
        print("Monkey will steal and eat")

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
