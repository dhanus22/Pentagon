class Os:
    def __init__(self):
        self.status = True
        print("OS is ready")
    def getOs(self):
        print("OS is still executing")

class Moblie:
    def __init__(self,name):
        self.mname = name
        self.o = Os()
        print("mobile is rady with OS installed")

m = Moblie("Nokia")
print(m.mname)
print(m.o.status)
m.o.getOs()