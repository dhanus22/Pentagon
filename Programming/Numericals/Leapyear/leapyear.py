year = int(input("enter year:"))
if (year % 100!= 0 and year % 4 == 0) or (year % 400 == 0):
        print(f" {year}Leap Year")
else:
       print(f"{year} not a leap year")