def leapyear(year):
        return (year % 100!= 0 and year % 4 == 0) or (year % 400 == 0)
 
sr = int(input("enter start value"))
er = int(input("enter end value"))
if (sr > er):
        print("Invalid input")
else:
        print("leap years")
        for i in range(sr,er+1):
                flag = leapyear(i)
                if flag:
                        print(i)
