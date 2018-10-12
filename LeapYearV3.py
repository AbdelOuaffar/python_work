def LeapYear(year):
    if year >=400 == 0 and year % 400 == 0:
        print(year, True)
    elif year in range(100,400) and year % 100 == 0:
        print (year, True)

    elif year in range(0, 100) and year % 4 == 0:
        print(year, True)
    else:
        print (year, False)
year=  int(input("Enter a year  :"))
Answer=  LeapYear(year)