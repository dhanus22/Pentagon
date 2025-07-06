class Hero:
    def __init__(self):
        self.name = "yash"
        self.age = 33
        self.height = 5.6
        self.mob = 9632

    def act(self):
        print("yash is acting")
    def dance(self):
        print("Yash is dancing")

h1 = Hero()
print(h1.name)
print(h1.age)
print(h1.height)
print(h1.mob)

h1.mob = 3206
h1.age = 35

h1.noOfMovies = 35
h1.noOfHits = 30

h2 = h1
h3 = h2

print(h3.name)
print(h2.height)
print(h1.age)
print(h1.mob)
print(h3.noOfMovies)
print(h2.noOfHits)
h3.act()
h1.dance()