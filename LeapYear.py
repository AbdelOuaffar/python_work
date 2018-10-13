def leapYear(YEAR):
    if year >= 400 and year % 400 == 0:
        print (True)
    elif year in range (100,400) and year % 100 == 0:
        print (True)
    elif year in range (0,100) and year % 4 == 0:
        print (True)
    else:
        print (False)
year = int(input("Enter year  :"))
leapYear(year)