class Student:
    def __init__(self,sname,susn,smob,saddr):
        self.name = sname
        self.usn = susn
        self.mob = smob
        self.addr = saddr

S1 = Student("rama","001",99101,"Blore")
S2 = Student("sita","002",99901,"Myo")
print(S1.mob)
print(S2.addr)

