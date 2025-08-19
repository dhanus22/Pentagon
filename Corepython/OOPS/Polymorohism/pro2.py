class Animal:
    def eat(self):
        print("Animal is takeoff")
    def sleep(self):
        print("Animal is flying")
    def breath(self):
        print("Animal is landing")

class Tiger(Animal):
    def eat(self):
        print("Tiger is takeoff")
    def sleep(self):
        print("Tiger is flying")
    def breath(self):
        print("Tiger is landing")

class Deer(Animal):
    def eat(self):
        print("Deer is takeoff")
    def sleep(self):
        print("Deer is flying")
    def breath(self):
        print("Deer is landing")

class Monkey(Animal):
    def eat(self):
        print("Monkey is takeoff")
    def sleep(self):
        print("Monkey is flying")
    def breath(self):
        print("Monkey is landing")

def allowPlanes(ref):
    ref.eat()
    ref.sleep()
    ref.breath()

c = Tiger()
p = Deer()
f = Monkey()

allowPlanes(c)
allowPlanes(p)
allowPlanes(f)

