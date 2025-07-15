class Farmer:
    r = 2.5
    def __init__(self,p1,t1):
        self.p = p1
        self.t1 = t1

    def disp(self):
        si = (self.p * self.t * Farmer.r) / 100 
        print(si)

f1 = Farmer(100000,2)
f2 = Farmer(200000,3)
f3 = Farmer(500000,5)
f1.disp()
f2.disp()
f3.disp()