# check leap year

year = int(input("Enter year to check whether its leapyear or not: "))

# if 
if year % 400 ==0 or (year % 4 == 0 and year % 100 != 0):
    print("laep year")

else:
    print("Not a leap year")