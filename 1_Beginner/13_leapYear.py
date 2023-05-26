"""
Leap Year is a year which is divisible by 4, except every year that is divisible by 100, but if the 
year is divisible by 400 then it leap. 

eg - 2000 / 4 = 500 (So leap), 2000 / 100 = 20 (So not leap), 2000 / 400 = 5 (So leap year)

"""


year = int(input("Enter a year of your choice = "))
if year % 4 == 0 and year % 100 != 0:
    print(year," is leap")
elif year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print(year," is leap")
    else:
        print(year," is not leap")