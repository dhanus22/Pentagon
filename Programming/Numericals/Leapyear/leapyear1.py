def leapyear(year):
        return (year % 100!= 0 and year % 4 == 0) or (year % 400 == 0)
 
year = int(input("enter year:"))
flag = leapyear(year)
if flag:
       print(f" {year}Leap Year")
else:
       print(f"{year} not a leap year")